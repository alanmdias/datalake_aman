# 04 — Arquitetura Alvo

## Arquitetura atual — Etapa 1 (em andamento)

```
San Marino
    └── PostgreSQL sm_teste (192.168.16.11:5432)
            └── [VPN obrigatória]
                    └── backup.py (execução manual pelo Alan)
                            └── Google Drive — Data Lake Aman
                                    ├── tabela.xlsx
                                    ├── tabelagrande_part01.csv
                                    └── ...
```

Extração manual, arquivo por tabela, sem transformações. Google Drive como destino intermediário — não é o destino final da arquitetura.

---

## Arquitetura alvo — Etapa 2

```
San Marino
    └── PostgreSQL sm_teste (acesso via VPN)
            └── Pipeline automatizado
                    ├── Camada Bronze (dados brutos, particionados por data)
                    ├── Camada Silver (dados limpos e tipados)
                    └── Camada Gold (entidades de negócio modeladas)
                            └── Banco relacional próprio da AMAN
                                    └── Claude (consultas e análises)
```

A infraestrutura cloud da AMAN ainda será definida. Candidatos naturais:
- **GCP + BigQuery** — integração nativa com Google Drive e com Claude via Vertex AI
- **AWS + Redshift ou Athena** — mais flexível, curva maior

---

## Arquitetura alvo — Etapas 3 e 4

```
Camada Gold (dados modelados)
    └── Documentação de entidades (Markdown)
            └── Claude com acesso estruturado à base
                    └── Motor de análise de crédito
```

O objetivo final é permitir que a AMAN consulte 35 anos de dados via linguagem natural e construa modelos de crédito proprietários sobre essa base.

---

## Considerações arquiteturais importantes

### Dependência de VPN
O banco da San Marino só é acessível via VPN. Qualquer pipeline automatizado precisa rodar em uma máquina permanentemente conectada à VPN — seja um servidor interno da San Marino, uma VM na rede deles, ou uma solução de tunelamento. Isso deve ser endereçado na Etapa 2.

### Volume de dados
A tabela `tabelapreco` tem 22M de linhas e crescerá. Qualquer pipeline futuro deve tratar tabelas grandes com extração incremental, não full-load.

### Tabelas vazias
93 das 357 tabelas estão vazias. Antes da Etapa 3, é importante entender se são módulos desativados, funcionalidades não utilizadas pela San Marino, ou tabelas que deveriam ter dados mas não têm.

### Backup incremental
O backup atual é um snapshot completo (full-load). Para atualizações recorrentes, será necessário mapear colunas de data de modificação em cada tabela relevante. Isso ainda não foi feito.

### Google Drive como destino intermediário
O Drive é adequado para a Etapa 1 (backup histórico acessível). Não é adequado como destino final de uma arquitetura de dados — não suporta consultas SQL, controle de versão de esquema, ou pipelines eficientes. A Etapa 2 define o destino definitivo.

---

## Sugestões arquiteturais (registradas para decisão futura)

1. **GCP como cloud preferencial** — a conta Google já está configurada (projeto `datalake-aman`), o Drive já é o destino atual, e BigQuery tem integração nativa com o ecossistema Gemini/Claude. Reduz fricção na Etapa 4.

2. **Particionamento por `data_referencia`** — ao ingerir no Data Lake, particionar as tabelas por data facilita queries e reduz custo de processamento.

3. **Nomenclatura padronizada das camadas** — sugestão: `aman-bronze`, `aman-silver`, `aman-gold` como datasets no BigQuery ou prefixos no S3.

4. **Inventário como contrato** — o `inventario_backup.xlsx` pode evoluir para um catálogo de dados formal (ex: DataHub, OpenMetadata) na Etapa 3.
