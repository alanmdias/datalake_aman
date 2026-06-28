"""
Reorganiza os arquivos no Google Drive para a seguinte estrutura:

  Data Lake Aman/
  └── Backup San Marino — Jun 2026/
      ├── Dados/         ← tabelas com dados (xlsx e csv)
      └── Vazias/        ← tabelas sem dados (xlsx vazio)

Idempotente: verifica se pastas/arquivos já existem antes de criar/mover.
"""
import os
import math
from dotenv import load_dotenv
import psycopg2
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(ROOT, ".env"))

GDRIVE_ROOT_ID = "0AEEhSxpe_XHHUk9PVA"
SCOPES = ["https://www.googleapis.com/auth/drive"]
TOKEN_FILE = os.path.join(ROOT, "token.json")
SCHEMA = "sm"
EXCEL_ROW_LIMIT = 900_000
CSV_CHUNK_SIZE = 1_000_000

FOLDER_BACKUP = "Backup San Marino — Jun 2026"
FOLDER_DADOS = "Dados"
FOLDER_VAZIAS = "Vazias"


def get_drive_service():
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
    return build("drive", "v3", credentials=creds)


def get_or_create_folder(service, name, parent_id):
    """Retorna o ID de uma pasta, criando-a se não existir."""
    query = (
        f"name='{name}' and '{parent_id}' in parents "
        f"and mimeType='application/vnd.google-apps.folder' and trashed=false"
    )
    result = service.files().list(
        q=query, fields="files(id, name)",
        supportsAllDrives=True, includeItemsFromAllDrives=True,
    ).execute()
    files = result.get("files", [])
    if files:
        print(f"  Pasta existente: {name} (id={files[0]['id']})")
        return files[0]["id"]
    folder = service.files().create(
        body={"name": name, "mimeType": "application/vnd.google-apps.folder", "parents": [parent_id]},
        fields="id", supportsAllDrives=True,
    ).execute()
    print(f"  Pasta criada: {name} (id={folder['id']})")
    return folder["id"]


def list_files_in_folder(service, folder_id):
    """Lista arquivos (não pastas) em uma pasta do Drive."""
    files = {}
    page_token = None
    while True:
        response = service.files().list(
            q=f"'{folder_id}' in parents and trashed=false and mimeType != 'application/vnd.google-apps.folder'",
            fields="nextPageToken, files(id, name)",
            supportsAllDrives=True, includeItemsFromAllDrives=True,
            pageToken=page_token, pageSize=1000,
        ).execute()
        for f in response.get("files", []):
            files[f["name"]] = f["id"]
        page_token = response.get("nextPageToken")
        if not page_token:
            break
    return files


def move_file(service, file_id, new_parent_id, current_parent_id):
    """Move um arquivo para outra pasta."""
    service.files().update(
        fileId=file_id,
        addParents=new_parent_id,
        removeParents=current_parent_id,
        supportsAllDrives=True,
        fields="id, parents",
    ).execute()


def get_expected_files(table, row_count):
    if row_count <= EXCEL_ROW_LIMIT:
        return [f"{table}.xlsx"]
    chunks = math.ceil(row_count / CSV_CHUNK_SIZE)
    if chunks == 1:
        return [f"{table}.csv"]
    return [f"{table}_part{i:02d}.csv" for i in range(1, chunks + 1)]


def main():
    print("Conectando ao PostgreSQL...")
    conn = psycopg2.connect(
        host=os.getenv("PG_HOST"), port=os.getenv("PG_PORT"),
        dbname=os.getenv("PG_DB"), user=os.getenv("PG_USER"),
        password=os.getenv("PG_PASSWORD"), connect_timeout=10,
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT table_name FROM information_schema.tables "
        "WHERE table_schema = %s AND table_type = 'BASE TABLE' ORDER BY table_name",
        (SCHEMA,),
    )
    tables = [r[0] for r in cur.fetchall()]

    print("Contando linhas por tabela...")
    table_counts = {}
    for t in tables:
        cur.execute(f'SELECT COUNT(*) FROM "{SCHEMA}"."{t}"')
        table_counts[t] = cur.fetchone()[0]
    conn.close()

    print("\nAutenticando no Google Drive...")
    service = get_drive_service()

    # Cria estrutura de pastas
    print("\nCriando estrutura de pastas...")
    folder_backup_id = get_or_create_folder(service, FOLDER_BACKUP, GDRIVE_ROOT_ID)
    folder_dados_id = get_or_create_folder(service, FOLDER_DADOS, folder_backup_id)
    folder_vazias_id = get_or_create_folder(service, FOLDER_VAZIAS, folder_backup_id)

    # Lista arquivos atualmente na raiz
    print("\nListando arquivos na pasta raiz do Drive...")
    root_files = list_files_in_folder(service, GDRIVE_ROOT_ID)
    print(f"  {len(root_files)} arquivos encontrados na raiz")

    # Move cada arquivo para a pasta correta
    moved_dados = 0
    moved_vazias = 0
    not_found = []

    print("\nMovendo arquivos...")
    for table, count in table_counts.items():
        expected = get_expected_files(table, count)
        dest_id = folder_vazias_id if count == 0 else folder_dados_id
        dest_name = FOLDER_VAZIAS if count == 0 else FOLDER_DADOS

        for fname in expected:
            if fname in root_files:
                move_file(service, root_files[fname], dest_id, GDRIVE_ROOT_ID)
                if count == 0:
                    moved_vazias += 1
                else:
                    moved_dados += 1
                print(f"  → {fname}  →  {dest_name}/")
            else:
                not_found.append(fname)

    print(f"\n{'='*60}")
    print(f"REORGANIZAÇÃO CONCLUÍDA")
    print(f"{'='*60}")
    print(f"  Movidos para {FOLDER_DADOS}/:  {moved_dados} arquivo(s)")
    print(f"  Movidos para {FOLDER_VAZIAS}/: {moved_vazias} arquivo(s)")
    if not_found:
        print(f"\n  ATENÇÃO — arquivos não encontrados na raiz ({len(not_found)}):")
        for f in not_found:
            print(f"    {f}")


if __name__ == "__main__":
    main()
