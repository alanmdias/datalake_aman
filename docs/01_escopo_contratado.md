# 01 — Escopo Contratado

O projeto foi aprovado comercialmente e está dividido em quatro etapas.

---

## Etapa 1 — Extração, Inventário e Backup

**Status: EM ANDAMENTO**

Esta etapa foi priorizada pelo cliente. O objetivo é garantir que a AMAN tenha uma cópia própria da base histórica da San Marino o quanto antes, reduzindo o risco de perda de acesso.

Atividades:
- Acesso VPN ao servidor da San Marino
- Conexão ao PostgreSQL
- Inventário das tabelas e volumes
- Exportação dos dados (Excel para tabelas normais, CSV para tabelas grandes)
- Backup no Google Drive corporativo da AMAN

**O que foi entregue:**
- Script `backup.py` com todas as funcionalidades acima
- Repositório GitHub configurado com `.gitignore` adequado
- Backup completo das 357 tabelas do schema `sm`
- Excel de inventário (`inventario_backup.xlsx`)
- Documentação técnica em `docs/`

---

## Etapa 2 — Estruturação da Arquitetura de Dados

**Status: Não iniciado**

Inclui:
- Definição da arquitetura cloud da AMAN
- Configuração da infraestrutura (provavelmente GCP/BigQuery ou AWS)
- Estruturação do Data Lake com camadas bronze/silver/gold
- Banco relacional próprio
- Pipelines de atualização automatizados
- Documentação operacional

---

## Etapa 3 — Modelagem e Preparação para IA

**Status: Não iniciado**

Inclui:
- Documentação das entidades do negócio (lotes, clientes, contratos, cobranças, etc.)
- Identificação e mapeamento dos relacionamentos entre tabelas
- Documentação em Markdown estruturada para consumo por IA
- Preparação da base para exploração via Claude

---

## Etapa 4 — Integração com Claude

**Status: Não iniciado**

Inclui:
- Configuração da integração do Claude com a base de dados da AMAN
- Testes e validação das capacidades de consulta
- Treinamento do time para uso
