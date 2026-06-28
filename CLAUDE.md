# CLAUDE.md — Contexto Permanente do Projeto

## Papel do Claude neste projeto

Atue como **Tech Lead e Arquiteto de Dados**.

Antes de implementar qualquer funcionalidade:
- Entenda o impacto na arquitetura
- Proponha melhorias quando pertinente
- Identifique riscos
- Mantenha a documentação sincronizada com o código

Sempre priorize qualidade da arquitetura em vez de apenas gerar código.

---

## Sobre a empresa

**AMAN** — fintech em fase inicial focada em crédito para o mercado de Real Estate.

Objetivo central: construir um motor proprietário de análise de crédito para compra de carteiras de recebíveis de loteamentos.

A empresa recebeu acesso a uma base histórica de ~35 anos de dados da **San Marino** (sistema de gestão imobiliária). Essa base é o principal ativo de dados da AMAN e a razão de existir deste projeto.

A AMAN ainda não possui infraestrutura própria de dados. Este projeto cria essa fundação do zero.

---

## Objetivo final do projeto

Criar a primeira arquitetura de dados da AMAN permitindo:

- Independência da infraestrutura da San Marino
- Armazenamento próprio dos dados
- Atualização automatizada
- Documentação técnica
- Exploração via Claude
- Preparação para futuras análises e modelos de crédito

---

## Escopo contratado — 4 etapas

| Etapa | Descrição | Status |
|-------|-----------|--------|
| 1 | Extração, inventário e backup da base histórica | **EM ANDAMENTO** |
| 2 | Estruturação da arquitetura de dados (cloud, data lake, pipelines) | Não iniciado |
| 3 | Modelagem e preparação para IA (entidades, relacionamentos, docs) | Não iniciado |
| 4 | Integração com Claude (configuração, testes, validação, treinamento) | Não iniciado |

---

## Estado atual — Etapa 1

### O que foi feito

Backup completo da base histórica da San Marino exportado para o Google Drive da AMAN.

| Resultado | Valor |
|-----------|-------|
| Total de tabelas no schema `sm` | 357 |
| Exportadas como Excel (.xlsx) | 256 |
| Exportadas como CSV dividido | 8 |
| Tabelas vazias | 93 |

### Arquivos no Drive

Pasta **Data Lake Aman** (ID: `0AEEhSxpe_XHHUk9PVA`) no Shared Drive organizacional da AMAN.

As 8 tabelas grandes (> 900k linhas) foram divididas em partes de 1M linhas:

| Tabela | Linhas | Partes |
|--------|--------|--------|
| tabelapreco | 22.093.029 | 23 |
| lcto | 6.863.769 | 7 |
| lotesvendap | 5.477.181 | 6 |
| saldos | 4.488.047 | 5 |
| custoarea | 2.063.028 | 3 |
| spedlote | 2.056.238 | 3 |
| lotesvendab | 1.938.202 | 2 |
| propostavendae | 1.239.107 | 2 |

---

## Arquitetura atual (Etapa 1)

```
San Marino
    └── PostgreSQL sm_teste (192.168.16.11:5432)
            └── [VPN obrigatória]
                    └── backup.py (execução manual)
                            └── Google Drive — Data Lake Aman
                                    ├── tabela.xlsx        (tabelas ≤ 900k linhas)
                                    ├── tabela_part01.csv  (tabelas > 900k linhas)
                                    └── ...
```

---

## Banco de dados de origem

- **Host:** 192.168.16.11:5432 — requer VPN ativa para conectar
- **Banco:** sm_teste
- **Schema exportado:** sm
- **Sistema de origem:** San Marino (ERP imobiliário)
- **Credenciais:** ficam em `.env` — nunca commitar

---

## Google Drive

- **Pasta:** Data Lake Aman — ID `0AEEhSxpe_XHHUk9PVA`
- **Tipo:** Shared Drive organizacional (AMAN) — não é Drive pessoal
- **API:** Drive API v3, OAuth2, escopo `https://www.googleapis.com/auth/drive`
- **Projeto GCP:** `datalake-aman`
- **Conta autorizada:** alandias.m@gmail.com
- **Atenção:** toda chamada à API exige `supportsAllDrives=True` e `includeItemsFromAllDrives=True`

---

## Estrutura do repositório

```
datalake_aman/
├── CLAUDE.md                        # Este arquivo — contexto permanente
├── BACKLOG.md                       # Backlog por etapa (To Do / Doing / Done)
├── DECISIONS.md                     # Registro de decisões arquiteturais
├── README.md                        # Visão geral do projeto
├── requirements.txt                 # Dependências Python
├── .env.example                     # Template de variáveis de ambiente
├── .env                             # Credenciais locais (NÃO commitado)
├── credentials.json                 # OAuth2 Google (NÃO commitado)
├── token.json                       # Token OAuth2 em cache (NÃO commitado)
├── progress.txt                     # Controle de progresso do backup (runtime)
├── scripts/
│   └── etapa1/
│       ├── backup.py                        # Exportação principal para o Drive
│       ├── etapa1_verificar.py              # Verifica alinhamento banco vs Drive
│       ├── etapa1_reorganizar_drive.py      # Reorganiza pastas no Drive
│       ├── etapa1_completar_tabelapreco.py  # Exportou parts faltantes (uso pontual)
│       └── etapa1_data_catalog.py           # Gera data catalog (xlsx + md)
└── docs/
    ├── 00_contexto_projeto.md
    ├── 01_escopo_contratado.md
    ├── 02_status_atual.md
    ├── 03_inventario_banco.md
    ├── 04_arquitetura_alvo.md
    ├── 05_proximos_passos.md
    ├── data_catalog.md
    └── relatorio_conclusao_etapa1.md
```

---

## Lógica do backup.py

| Condição | Formato | Naming |
|----------|---------|--------|
| 0 linhas | Excel vazio | `tabela.xlsx` |
| 1 – 900.000 linhas | Excel | `tabela.xlsx` |
| > 900.000 linhas | CSV em partes de 1M linhas | `tabela_part01.csv`, `tabela_part02.csv`, … |

**Retomada:** o `progress.txt` registra cada tabela concluída. Para reprocessar uma tabela específica, remover seu nome do arquivo e rodar novamente.

---

## Como rodar o backup

```powershell
# 1. Garantir VPN conectada (host 192.168.16.11)
cd C:\Users\Alan\datalake_aman
python scripts/etapa1/backup.py
# Na primeira execução: autenticação OAuth2 abre no browser
```

---

## Diretrizes de desenvolvimento

- Código limpo e reutilizável
- Scripts idempotentes (rodar duas vezes não gera estado incorreto)
- Arquitetura modular
- Nenhuma credencial no repositório — usar `.env`
- Documentação obrigatória ao criar qualquer funcionalidade
- Registrar decisões importantes em `docs/06_decisoes_tecnicas.md`

Sempre que criar ou modificar uma funcionalidade:
1. Atualizar a documentação correspondente em `docs/`
2. Explicar a decisão tomada
3. Manter `CLAUDE.md` sincronizado com o estado real do projeto

---

## Pessoas

- **Alan Dias** (alandias.m@gmail.com) — responsável técnico, ponto de contato principal
