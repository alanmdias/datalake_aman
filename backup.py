import os
import io
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
import psycopg2
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# ── Configuração ──────────────────────────────────────────────────────────────
GDRIVE_FOLDER_ID = "0AEEhSxpe_XHHUk9PVA"
SCOPES = ["https://www.googleapis.com/auth/drive.file"]
TOKEN_FILE = "token.json"
CREDENTIALS_FILE = "credentials.json"

DB_CONFIG = {
    "host": os.getenv("PG_HOST", "localhost"),
    "port": os.getenv("PG_PORT", "5432"),
    "dbname": os.getenv("PG_DB"),
    "user": os.getenv("PG_USER"),
    "password": os.getenv("PG_PASSWORD"),
}

# Deixe vazio para exportar TODAS as tabelas do schema
TABLES_TO_EXPORT = []
SCHEMA = "sm"
# ─────────────────────────────────────────────────────────────────────────────


def get_drive_service():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as f:
            f.write(creds.to_json())
    return build("drive", "v3", credentials=creds)


def list_tables(conn):
    if TABLES_TO_EXPORT:
        return TABLES_TO_EXPORT
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT table_name FROM information_schema.tables
            WHERE table_schema = %s AND table_type = 'BASE TABLE'
            ORDER BY table_name
            """,
            (SCHEMA,),
        )
        return [row[0] for row in cur.fetchall()]


def table_to_excel_bytes(conn, table: str) -> bytes:
    df = pd.read_sql(f'SELECT * FROM "{SCHEMA}"."{table}"', conn)
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name=table[:31])
    return buffer.getvalue()


def upload_to_drive(service, filename: str, content: bytes):
    query = (
        f"name='{filename}' and '{GDRIVE_FOLDER_ID}' in parents and trashed=false"
    )
    existing = service.files().list(q=query, fields="files(id)").execute().get("files", [])

    media = MediaIoBaseUpload(
        io.BytesIO(content),
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        resumable=True,
    )
    if existing:
        file_id = existing[0]["id"]
        service.files().update(fileId=file_id, media_body=media).execute()
        print(f"  Atualizado: {filename}")
    else:
        metadata = {"name": filename, "parents": [GDRIVE_FOLDER_ID]}
        service.files().create(body=metadata, media_body=media, fields="id").execute()
        print(f"  Criado:     {filename}")


def main():
    print("Conectando ao PostgreSQL...")
    conn = psycopg2.connect(**DB_CONFIG)

    print("Autenticando no Google Drive...")
    service = get_drive_service()

    tables = list_tables(conn)
    print(f"\n{len(tables)} tabela(s) encontrada(s): {tables}\n")

    for table in tables:
        print(f"Exportando '{table}'...")
        excel_bytes = table_to_excel_bytes(conn, table)
        upload_to_drive(service, f"{table}.xlsx", excel_bytes)

    conn.close()
    print("\nBackup concluído!")


if __name__ == "__main__":
    main()
