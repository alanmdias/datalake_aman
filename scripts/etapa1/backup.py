import os
import io
import warnings
from dotenv import load_dotenv
import pandas as pd
import psycopg2
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(ROOT, ".env"))
warnings.filterwarnings("ignore")

# ── Configuração ──────────────────────────────────────────────────────────────
GDRIVE_FOLDER_ID = "0AEEhSxpe_XHHUk9PVA"
SCOPES = ["https://www.googleapis.com/auth/drive"]
TOKEN_FILE = os.path.join(ROOT, "token.json")
CREDENTIALS_FILE = os.path.join(ROOT, "credentials.json")
PROGRESS_FILE = os.path.join(ROOT, "progress.txt")

DB_CONFIG = {
    "host": os.getenv("PG_HOST", "localhost"),
    "port": os.getenv("PG_PORT", "5432"),
    "dbname": os.getenv("PG_DB"),
    "user": os.getenv("PG_USER"),
    "password": os.getenv("PG_PASSWORD"),
}

TABLES_TO_EXPORT = []  # vazio = exporta todas
SCHEMA = "sm"
EXCEL_ROW_LIMIT = 900_000  # acima disso exporta como CSV
CSV_CHUNK_SIZE = 1_000_000  # linhas por arquivo CSV
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


def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE) as f:
            return set(line.strip() for line in f if line.strip())
    return set()


def save_progress(table):
    with open(PROGRESS_FILE, "a") as f:
        f.write(table + "\n")


def df_to_excel_bytes(df, sheet_name):
    for col in df.select_dtypes(include=["datetimetz"]).columns:
        df[col] = df[col].dt.tz_localize(None)
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name=sheet_name[:31])
    return buffer.getvalue()


def upload_to_drive(service, filename, content, mimetype):
    query = f"name='{filename}' and '{GDRIVE_FOLDER_ID}' in parents and trashed=false"
    existing = (
        service.files()
        .list(q=query, fields="files(id)", supportsAllDrives=True, includeItemsFromAllDrives=True)
        .execute()
        .get("files", [])
    )
    media = MediaIoBaseUpload(io.BytesIO(content), mimetype=mimetype, resumable=True)
    if existing:
        service.files().update(fileId=existing[0]["id"], media_body=media, supportsAllDrives=True).execute()
        print(f"  Atualizado: {filename}")
    else:
        service.files().create(
            body={"name": filename, "parents": [GDRIVE_FOLDER_ID]},
            media_body=media, fields="id", supportsAllDrives=True,
        ).execute()
        print(f"  Criado:     {filename}")


def df_to_csv_bytes(df):
    return df.to_csv(index=False).encode("utf-8-sig")


def export_table(conn, service, table):
    with conn.cursor() as cur:
        cur.execute(f'SELECT COUNT(*) FROM "{SCHEMA}"."{table}"')
        total = cur.fetchone()[0]

    if total <= EXCEL_ROW_LIMIT:
        df = pd.read_sql(f'SELECT * FROM "{SCHEMA}"."{table}"', conn)
        content = df_to_excel_bytes(df, table)
        upload_to_drive(service, f"{table}.xlsx", content,
                        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    else:
        chunks = (total + CSV_CHUNK_SIZE - 1) // CSV_CHUNK_SIZE
        print(f"  Tabela grande ({total:,} linhas) — dividindo em {chunks} CSV(s)...")
        offset = 0
        part = 1
        while offset < total:
            df_chunk = pd.read_sql(
                f'SELECT * FROM "{SCHEMA}"."{table}" LIMIT {CSV_CHUNK_SIZE} OFFSET {offset}',
                conn,
            )
            filename = f"{table}_part{part:02d}.csv" if chunks > 1 else f"{table}.csv"
            upload_to_drive(service, filename, df_to_csv_bytes(df_chunk), "text/csv")
            print(f"    parte {part}/{chunks} — {offset + len(df_chunk):,}/{total:,} linhas")
            offset += CSV_CHUNK_SIZE
            part += 1


def main():
    print("Conectando ao PostgreSQL...")
    conn = psycopg2.connect(**DB_CONFIG)

    print("Autenticando no Google Drive...")
    service = get_drive_service()

    tables = list_tables(conn)
    done = load_progress()
    pending = [t for t in tables if t not in done]

    print(f"\n{len(tables)} tabela(s) total | {len(done)} já concluídas | {len(pending)} restantes\n")

    for table in pending:
        print(f"Exportando '{table}'...")
        try:
            if conn.closed:
                conn = psycopg2.connect(**DB_CONFIG)
            export_table(conn, service, table)
            save_progress(table)
        except Exception as e:
            print(f"  ERRO em '{table}': {e} — pulando e continuando...")
            try:
                conn = psycopg2.connect(**DB_CONFIG)
            except Exception:
                pass

    conn.close()
    print("\nBackup concluído!")


if __name__ == "__main__":
    main()
