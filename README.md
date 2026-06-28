# AMAN — Data Lake

Fundação tecnológica de dados da **AMAN**, fintech focada em crédito para o mercado de Real Estate.

Este repositório contém os scripts, pipelines e documentação técnica do projeto de arquitetura de dados da AMAN, construído sobre a base histórica de ~35 anos da San Marino.

---

## Contexto

A AMAN recebeu acesso a uma base histórica da **San Marino** (ERP imobiliário), contendo dados operacionais de loteamentos: clientes, contratos, cobranças, inadimplência, financeiro, entre outros.

O projeto tem como objetivo criar a primeira arquitetura de dados proprietária da AMAN, permitindo independência da infraestrutura da San Marino e preparando a base para futuras análises de crédito e modelos de IA.

---

## Estrutura do projeto

```
datalake_aman/
├── scripts/
│   └── etapa1/
│       ├── backup.py                        # Exportação de todas as tabelas para o Drive
│       ├── etapa1_verificar.py              # Verifica alinhamento banco vs Drive
│       ├── etapa1_reorganizar_drive.py      # Reorganiza arquivos em subpastas no Drive
│       ├── etapa1_completar_tabelapreco.py  # Exportou parts faltantes (uso pontual)
│       └── etapa1_data_catalog.py           # Gera data_catalog.xlsx e docs/data_catalog.md
├── docs/
│   ├── 00_contexto_projeto.md
│   ├── 01_escopo_contratado.md
│   ├── 02_status_atual.md
│   ├── 03_inventario_banco.md
│   ├── 04_arquitetura_alvo.md
│   ├── 05_proximos_passos.md
│   ├── data_catalog.md
│   └── relatorio_conclusao_etapa1.md
├── requirements.txt
├── .env.example
├── CLAUDE.md
├── BACKLOG.md
└── DECISIONS.md
```

---

## Etapas do projeto

| Etapa | Descrição | Status |
|-------|-----------|--------|
| 1 | Extração, inventário e backup da base histórica | EM ANDAMENTO |
| 2 | Estruturação da arquitetura de dados | Não iniciado |
| 3 | Modelagem e preparação para IA | Não iniciado |
| 4 | Integração com Claude | Não iniciado |

---

## Etapa 1 — Backup para Google Drive

Exporta todas as tabelas do schema `sm` do PostgreSQL da San Marino para o Google Drive da AMAN.

**Regras de exportação:**

| Volume | Formato |
|--------|---------|
| Tabela vazia | `.xlsx` vazio |
| Até 900.000 linhas | `.xlsx` |
| Acima de 900.000 linhas | `.csv` dividido em partes de 1.000.000 linhas |

**Resultado da primeira execução (junho 2026):**

| | |
|-|-|
| Total de tabelas | 357 |
| Exportadas como Excel | 256 |
| Exportadas como CSV | 8 tabelas (51 arquivos) |
| Tabelas vazias | 93 |

### Pré-requisitos

- Python 3.10+
- VPN conectada ao servidor da San Marino (192.168.16.11)
- Projeto no Google Cloud com Drive API habilitada
- Arquivo `credentials.json` (OAuth2) na raiz do projeto

### Instalação

```bash
pip install -r requirements.txt
```

### Configuração

Copie `.env.example` para `.env` e preencha:

```
PG_HOST=192.168.16.11
PG_PORT=5432
PG_DB=sm_teste
PG_USER=seu_usuario
PG_PASSWORD=sua_senha
```

Coloque o `credentials.json` (OAuth2 do Google Cloud) na raiz do projeto.

### Execução

```powershell
cd datalake_aman
python scripts/etapa1/backup.py
```

Na primeira execução, um browser abrirá para autenticação OAuth2. O token é salvo em `token.json` para execuções futuras.

O script é **retomável**: se interrompido, continua de onde parou via `progress.txt`. Para reprocessar uma tabela específica, remova-a do `progress.txt`.

---

## Configuração de credenciais (Google Cloud)

1. Acesse [console.cloud.google.com](https://console.cloud.google.com)
2. Projeto: `datalake-aman`
3. Habilite a **Google Drive API**
4. Crie credenciais OAuth2 (tipo: Aplicativo de desktop)
5. Faça download do JSON e salve como `credentials.json` na raiz do projeto

> `credentials.json`, `token.json` e `.env` estão no `.gitignore` — nunca commitar.

---

## Documentação

Consulte a pasta `docs/` para detalhes de arquitetura, inventário, decisões técnicas e próximos passos.
