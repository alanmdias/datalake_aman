# DECISIONS — Registro de Decisões Arquiteturais

Registro das decisões técnicas e arquiteturais relevantes tomadas durante o projeto.  
Para cada decisão: contexto, alternativas consideradas, decisão tomada e justificativa.

---

## DEC-001 — Formato de exportação: Excel para tabelas pequenas, CSV para grandes

**Data:** junho 2026  
**Etapa:** 1  
**Status:** Vigente

**Contexto:**  
Precisávamos definir o formato de saída dos arquivos exportados para o Google Drive. O objetivo era que os arquivos fossem acessíveis para usuários não técnicos da AMAN.

**Alternativas consideradas:**
- CSV para todas as tabelas — simples, mas difícil de abrir diretamente
- Excel para todas as tabelas — limite de 1.048.576 linhas inviabiliza tabelas grandes
- Parquet — ideal para data lake, mas não acessível sem ferramentas específicas

**Decisão:**  
Excel (.xlsx) para tabelas até 900.000 linhas; CSV dividido em partes de 1.000.000 linhas para tabelas maiores.

**Justificativa:**  
Excel é o formato mais acessível para o perfil atual de usuários da AMAN. O limiar de 900k (e não 1.048.576) é uma margem de segurança. Parquet será considerado na Etapa 2, quando houver infraestrutura adequada para consumi-lo.

---

## DEC-002 — Mecanismo de retomada via arquivo de texto (progress.txt)

**Data:** junho 2026  
**Etapa:** 1  
**Status:** Vigente

**Contexto:**  
A exportação de 357 tabelas levava horas e dependia de VPN estável. Era necessário um mecanismo para retomar o processo sem reprocessar tabelas já concluídas.

**Alternativas consideradas:**
- Banco de dados SQLite de controle — mais robusto, mas desnecessariamente complexo
- Arquivo JSON com metadados — flexível, mas overkill para o caso
- Arquivo texto simples com um nome por linha — suficiente e editável manualmente

**Decisão:**  
`progress.txt` com um nome de tabela por linha.

**Justificativa:**  
Simplicidade adequada ao problema. Fácil de inspecionar e editar manualmente para forçar reprocessamento de tabelas específicas. Adequado para execuções pontuais — não para pipelines contínuos.

---

## DEC-003 — Leitura em chunks via LIMIT/OFFSET (não pandas chunksize)

**Data:** junho 2026  
**Etapa:** 1  
**Status:** Vigente

**Contexto:**  
Tabelas com milhões de linhas (ex: `tabelapreco` com 22M) causavam erro de memória ao tentar carregar tudo de uma vez via `pd.read_sql`.

**Alternativas consideradas:**
- `pd.read_sql` com `chunksize` — iterador, mas pode alocar memória de forma imprevisível dependendo do driver
- `LIMIT/OFFSET` no SQL — controle explícito de quantas linhas são transferidas do banco

**Decisão:**  
`LIMIT/OFFSET` no SQL, lendo `CSV_CHUNK_SIZE = 1.000.000` linhas por vez.

**Justificativa:**  
LIMIT/OFFSET garante que apenas o chunk requisitado trafega entre banco e Python. Mais previsível em termos de consumo de memória. A desvantagem (possível inconsistência em tabelas com inserts concorrentes) é irrelevante aqui, pois o banco é de produção da San Marino e não sofre writes durante a exportação.

---

## DEC-004 — Escopo OAuth2 completo (drive) em vez de drive.file

**Data:** junho 2026  
**Etapa:** 1  
**Status:** Vigente

**Contexto:**  
A autenticação Google Drive precisa de um escopo OAuth2. O escopo restrito `drive.file` só permite acesso a arquivos criados pelo próprio app.

**Alternativas consideradas:**
- `drive.file` — mais seguro, mas impede acesso a pastas pré-existentes
- `drive` (escopo completo) — acesso total ao Drive do usuário autenticado

**Decisão:**  
Escopo `https://www.googleapis.com/auth/drive` (completo).

**Justificativa:**  
A pasta de destino (`Data Lake Aman`) foi criada pela organização e compartilhada com o Alan. Com `drive.file`, a API retornava 404. Como a conta autenticada é pessoal (alandias.m@gmail.com) e o token não é compartilhado, o risco de escopo amplo é aceitável.

---

## DEC-005 — supportsAllDrives=True em todas as chamadas à Drive API

**Data:** junho 2026  
**Etapa:** 1  
**Status:** Vigente

**Contexto:**  
A pasta `Data Lake Aman` está em um Shared Drive organizacional da AMAN, não no Drive pessoal do Alan.

**Decisão:**  
Adicionar `supportsAllDrives=True` e `includeItemsFromAllDrives=True` em todas as chamadas `list()`, `create()` e `update()` da Drive API.

**Justificativa:**  
Sem esses parâmetros, a API v3 retorna 404 ao tentar acessar qualquer item em Shared Drives. É um requisito obrigatório da API, não uma escolha.

---

## DEC-006 — Strip de timezone em colunas datetime antes de escrever no Excel

**Data:** junho 2026  
**Etapa:** 1  
**Status:** Vigente

**Contexto:**  
Colunas `timestamptz` do PostgreSQL chegam ao pandas como `DatetimeTZDtype`. O `openpyxl` não suporta datetimes com timezone e lança `ValueError`.

**Decisão:**  
Aplicar `df[col].dt.tz_localize(None)` em todas as colunas `datetimetz` antes de escrever no Excel.

**Justificativa:**  
Remove a informação de timezone mas preserva o valor horário. O banco usa UTC, então não há perda de informação relevante para o contexto de negócio da AMAN. Alternativa (converter para string) perderia o tipo datetime no Excel.

---

## DEC-007 — Cloud provider agnóstico até decisão formal na Etapa 2

**Data:** junho 2026  
**Etapa:** 1 → 2  
**Status:** Vigente

**Contexto:**  
Durante a Etapa 1, surgiu a questão de qual cloud provider usar para a infraestrutura definitiva da AMAN na Etapa 2.

**Alternativas consideradas:**
- GCP — sinergia com conta Google já configurada, integração com BigQuery e Vertex AI
- AWS — maior market share, mais opções de ferramentas
- Azure — menos relevante para o perfil da AMAN

**Decisão:**  
Manter o projeto agnóstico de cloud provider até a Etapa 2, quando os requisitos estarão melhor definidos.

**Justificativa:**  
A decisão de infraestrutura tem impacto de longo prazo e custo significativo. Tomá-la sem requisitos completos seria precipitado. A documentação e o código da Etapa 1 não assumem nenhum provider específico. A Etapa 2 iniciará com um processo formal de definição de requisitos antes de qualquer escolha.
