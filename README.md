# datalake_aman

Backup automático de tabelas PostgreSQL para o Google Drive em formato Excel (.xlsx).

## Pré-requisitos

- Python 3.10+
- Acesso ao banco PostgreSQL
- Projeto no Google Cloud com a Drive API habilitada e `credentials.json` de OAuth2

## Instalação

```bash
pip install -r requirements.txt
```

## Configuração

1. Copie `.env.example` para `.env` e preencha as variáveis do banco:
   ```
   PG_HOST=localhost
   PG_PORT=5432
   PG_DB=nome_do_banco
   PG_USER=seu_usuario
   PG_PASSWORD=sua_senha
   ```

2. Coloque o arquivo `credentials.json` (OAuth2 do Google Cloud) na raiz do projeto.

3. Na primeira execução, um navegador abrirá para autenticação. O token será salvo em `token.json` para execuções futuras.

## Uso

```bash
# Carregar variáveis de ambiente (Windows PowerShell)
$env:PG_HOST="localhost"; $env:PG_DB="meu_banco"; $env:PG_USER="user"; $env:PG_PASSWORD="senha"

python backup.py
```

## Exportar tabelas específicas

No `backup.py`, edite a variável `TABLES_TO_EXPORT`:

```python
TABLES_TO_EXPORT = ["clientes", "pedidos", "produtos"]
```

Deixe a lista vazia `[]` para exportar todas as tabelas do schema `public`.

## Credenciais Google Cloud

1. Acesse [console.cloud.google.com](https://console.cloud.google.com)
2. Crie um projeto → habilite a **Google Drive API**
3. Crie credenciais OAuth2 (tipo: **Aplicativo de desktop**)
4. Faça download do JSON e renomeie para `credentials.json`
