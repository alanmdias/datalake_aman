"""
Exporta apenas as partes 22 e 23 da tabela tabelapreco para o Google Drive.
As partes 01-21 já estão no Drive e não serão retocadas.
"""
import os
import io
import warnings
from dotenv import load_dotenv
import pandas as pd
import psycopg2
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

load_dotenv()
warnings.filterwarnings("ignore")

GDRIVE_FOLDER_ID = "0AEEhSxpe_XHHUk9PVA"
SCOPES = ["https://www.googleapis.com/auth/drive"]
TOKEN_FILE = "token.json"
SCHEMA = "sm"
TABLE = "tabelapreco"
CSV_CHUNK_SIZE = 1_000_000
MISSING_PARTS = [22, 23]  # partes a exportar


def get_drive_service():
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
    return build("drive", "v3", credentials=creds)


def upload_to_drive(service, filename, content):
    query = f"name='{filename}' and '{GDRIVE_FOLDER_ID}' in parents and trashed=false"
    existing = service.files().list(
        q=query, fields="files(id)",
        supportsAllDrives=True, includeItemsFromAllDrives=True,
    ).execute().get("files", [])
    media = MediaIoBaseUpload(io.BytesIO(content), mimetype="text/csv", resumable=True)
    if existing:
        service.files().update(
            fileId=existing[0]["id"], media_body=media, supportsAllDrives=True,
        ).execute()
        print(f"  Atualizado: {filename}")
    else:
        service.files().create(
            body={"name": filename, "parents": [GDRIVE_FOLDER_ID]},
            media_body=media, fields="id", supportsAllDrives=True,
        ).execute()
        print(f"  Criado: {filename}")


def main():
    print("Conectando ao PostgreSQL...")
    conn = psycopg2.connect(
        host=os.getenv("PG_HOST"), port=os.getenv("PG_PORT"),
        dbname=os.getenv("PG_DB"), user=os.getenv("PG_USER"),
        password=os.getenv("PG_PASSWORD"),
    )

    print("Autenticando no Google Drive...")
    service = get_drive_service()

    for part in MISSING_PARTS:
        offset = (part - 1) * CSV_CHUNK_SIZE
        filename = f"{TABLE}_part{part:02d}.csv"
        print(f"\nExportando {filename} (offset={offset:,})...")

        df = pd.read_sql(
            f'SELECT * FROM "{SCHEMA}"."{TABLE}" LIMIT {CSV_CHUNK_SIZE} OFFSET {offset}',
            conn,
        )
        print(f"  {len(df):,} linhas lidas")
        content = df.to_csv(index=False).encode("utf-8-sig")
        upload_to_drive(service, filename, content)

    conn.close()
    print("\nConcluido!")


if __name__ == "__main__":
    main()
