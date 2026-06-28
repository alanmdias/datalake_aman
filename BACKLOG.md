# BACKLOG — AMAN Data Lake

Organizado por etapa do projeto conforme proposta comercial aprovada.

---

## DONE

### Etapa 1 — Extração, Inventário e Backup

- [x] Configurar acesso VPN ao servidor da San Marino
- [x] Estabelecer conexão com o PostgreSQL (`sm_teste`, schema `sm`)
- [x] Inventariar todas as tabelas do schema `sm` (357 tabelas identificadas)
- [x] Desenvolver script de exportação `backup.py`
- [x] Implementar exportação para Excel (.xlsx) para tabelas até 900k linhas
- [x] Implementar exportação para CSV para tabelas acima de 900k linhas
- [x] Implementar divisão de CSVs grandes em partes de 1M linhas
- [x] Implementar mecanismo de retomada via `progress.txt`
- [x] Implementar reconexão automática ao PostgreSQL em caso de queda
- [x] Configurar projeto Google Cloud (`datalake-aman`) e habilitar Drive API
- [x] Configurar autenticação OAuth2 com Google Drive
- [x] Exportar 357 tabelas para o Google Drive (pasta Data Lake Aman)
- [x] Gerar inventário `inventario_backup.xlsx` com status de cada tabela
- [x] Criar repositório GitHub `datalake_aman`
- [x] Configurar `.gitignore` (credenciais nunca commitadas)
- [x] Criar documentação técnica em `docs/`
- [x] Criar `CLAUDE.md` com contexto permanente do projeto

---

## DOING

### Etapa 1 — Finalização

- [ ] Verificar integridade: comparar tabelas no banco com arquivos no Drive
- [ ] Reorganizar Drive: mover arquivos para subpasta `Backup San Marino — Jun 2026/`
- [ ] Separar tabelas vazias em subpasta própria no Drive
- [ ] Gerar relatório de conclusão da Etapa 1 para o cliente (Mário)
- [ ] Commitar toda a documentação no GitHub
- [ ] Enviar relatório e comunicar conclusão da Etapa 1

---

## TO DO

### Etapa 2 — Estruturação da Arquitetura de Dados

**Decisões preliminares:**
- [ ] Definir cloud provider (agnóstico por enquanto — AWS, GCP ou Azure)
- [ ] Definir destino definitivo dos dados (Data Warehouse ou Data Lake)
- [ ] Definir estratégia de conectividade VPN para pipelines automatizados
- [ ] Definir frequência de atualização dos dados (diária, semanal, mensal)
- [ ] Definir estratégia de retenção histórica (snapshots vs. incremental)

**Implementação:**
- [ ] Configurar infraestrutura cloud da AMAN
- [ ] Criar estrutura de camadas bronze / silver / gold
- [ ] Desenvolver pipeline de ingestão da camada bronze (dados brutos)
- [ ] Desenvolver pipeline de transformação para camada silver (dados limpos)
- [ ] Implementar atualização incremental para tabelas grandes (> 900k linhas)
- [ ] Configurar agendamento e monitoramento dos pipelines
- [ ] Documentar arquitetura implementada

### Etapa 3 — Modelagem e Preparação para IA

- [ ] Mapear entidades centrais do negócio (cliente, contrato, lote, cobrança, inadimplência)
- [ ] Identificar e documentar relacionamentos entre tabelas
- [ ] Investigar as 93 tabelas vazias (módulos desativados ou dados ausentes?)
- [ ] Criar dicionário de dados em Markdown (tabela por tabela)
- [ ] Modelar camada gold com visões orientadas ao negócio
- [ ] Preparar documentação estruturada para consumo por IA

### Etapa 4 — Integração com Claude

- [ ] Definir modo de acesso do Claude à base estruturada
- [ ] Configurar integração técnica
- [ ] Desenvolver prompts e contextos de negócio
- [ ] Testar capacidades de consulta e análise
- [ ] Validar resultados com o time da AMAN
- [ ] Realizar treinamento com os usuários

---

## Notas

- O projeto deve permanecer **agnóstico de cloud provider** até decisão formal na Etapa 2
- Toda nova funcionalidade deve ter documentação correspondente em `docs/`
- Decisões arquiteturais relevantes devem ser registradas em `DECISIONS.md`
