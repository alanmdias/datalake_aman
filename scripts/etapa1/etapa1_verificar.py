"""
Verifica se o Google Drive reflete o estado atual do banco de dados.
Compara as tabelas do schema sm com os arquivos presentes no Drive.
"""
import os
import math
import io
from dotenv import load_dotenv
import psycopg2
import pandas as pd
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(ROOT, ".env"))

GDRIVE_FOLDER_ID = "0AEEhSxpe_XHHUk9PVA"
SCOPES = ["https://www.googleapis.com/auth/drive"]
TOKEN_FILE = os.path.join(ROOT, "token.json")
SCHEMA = "sm"
EXCEL_ROW_LIMIT = 900_000
CSV_CHUNK_SIZE = 1_000_000


def get_drive_service():
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
    return build("drive", "v3", credentials=creds)


def list_drive_files(service):
    """Lista todos os arquivos na pasta raiz do Drive (não recursivo)."""
    files = []
    page_token = None
    while True:
        response = service.files().list(
            q=f"'{GDRIVE_FOLDER_ID}' in parents and trashed=false",
            fields="nextPageToken, files(id, name, mimeType)",
            supportsAllDrives=True,
            includeItemsFromAllDrives=True,
            pageToken=page_token,
            pageSize=1000,
        ).execute()
        files.extend(response.get("files", []))
        page_token = response.get("nextPageToken")
        if not page_token:
            break
    return {f["name"]: f for f in files}


def get_expected_files(table, row_count, drive_files):
    """Retorna a lista de nomes de arquivo esperados para uma tabela.

    Para tabelas grandes exportadas como CSV único (formato legado, antes da divisão
    em partes ser implementada), aceita tanto o CSV único quanto os arquivos particionados.
    """
    if row_count <= EXCEL_ROW_LIMIT:
        return [f"{table}.xlsx"]
    chunks = math.ceil(row_count / CSV_CHUNK_SIZE)
    if chunks == 1:
        return [f"{table}.csv"]
    # Aceita CSV único legado se estiver no Drive
    if f"{table}.csv" in drive_files:
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

    print("Buscando tabelas no banco...")
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

    print("Autenticando no Google Drive...")
    service = get_drive_service()

    print("Listando arquivos no Drive...")
    drive_files = list_drive_files(service)

    # Analisa status por tabela
    missing = []       # arquivos esperados que não estão no Drive
    ok = []            # tabelas com todos os arquivos presentes
    extra_files = set(drive_files.keys())  # arquivos no Drive não esperados

    for table, count in table_counts.items():
        expected = get_expected_files(table, count, drive_files)
        table_ok = True
        for fname in expected:
            extra_files.discard(fname)
            if fname not in drive_files:
                missing.append((table, count, fname))
                table_ok = False
        if table_ok:
            ok.append(table)

    # Remove subpastas e outros arquivos conhecidos do "extra"
    extra_files = {f for f in extra_files if not drive_files[f]["mimeType"] == "application/vnd.google-apps.folder"}

    # Relatório
    print(f"\n{'='*60}")
    print(f"RELATÓRIO DE VERIFICAÇÃO — {len(tables)} tabelas no banco")
    print(f"{'='*60}")
    print(f"\n[OK]      Tabelas com todos os arquivos presentes: {len(ok)}")
    print(f"[FALTANDO] Tabelas com arquivos faltando:          {len(set(t for t,_,_ in missing))}")
    print(f"[EXTRA]   Arquivos no Drive nao reconhecidos:      {len(extra_files)}")

    if missing:
        print(f"\n{'-'*60}")
        print("ARQUIVOS FALTANDO NO DRIVE:")
        for table, count, fname in missing:
            print(f"  {fname}  (tabela: {table}, {count:,} linhas)")

    if extra_files:
        print(f"\n{'-'*60}")
        print("ARQUIVOS NO DRIVE NÃO RECONHECIDOS (podem ser de outra origem):")
        for f in sorted(extra_files):
            print(f"  {f}")

    # Exporta resultado para Excel
    rows = []
    for table, count in table_counts.items():
        expected = get_expected_files(table, count, drive_files)
        for fname in expected:
            rows.append({
                "Tabela": table,
                "Linhas": count,
                "Arquivo esperado": fname,
                "Presente no Drive": "Sim" if fname in drive_files else "NÃO",
            })

    df = pd.DataFrame(rows)
    output = os.path.join(ROOT, "verificacao_drive.xlsx")
    df.to_excel(output, index=False)
    print(f"\nResultado detalhado exportado para: {output}")


if __name__ == "__main__":
    main()
