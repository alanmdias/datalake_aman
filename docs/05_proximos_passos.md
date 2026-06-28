# 05 — Próximos Passos

## Etapa 1 — Itens finais (quase concluída)

- [ ] Commitar a documentação (`docs/` e `CLAUDE.md`) no GitHub
- [ ] Mover `inventario_backup.xlsx` para o Google Drive para acesso compartilhado pelo cliente
- [ ] Verificar no Drive se todos os arquivos CSV das 8 tabelas grandes estão íntegros

## Etapa 2 — Estruturação da arquitetura (próxima etapa)

Decisões a tomar antes de iniciar:

- [ ] Definir cloud provider (GCP recomendado — ver `04_arquitetura_alvo.md`)
- [ ] Definir destino definitivo dos dados (BigQuery? Postgres próprio? S3+Athena?)
- [ ] Definir estratégia de conectividade VPN para pipelines automatizados
- [ ] Definir frequência de atualização (diária? semanal?)

Atividades técnicas:

- [ ] Configurar projeto cloud da AMAN
- [ ] Criar estrutura de camadas bronze/silver/gold
- [ ] Desenvolver pipelines de ingestão a partir do backup do Drive (ou direto do PostgreSQL via VPN)
- [ ] Implementar atualização incremental para tabelas grandes
- [ ] Configurar agendamento e monitoramento dos pipelines

## Etapa 3 — Modelagem (após Etapa 2)

- [ ] Mapear entidades centrais do negócio (cliente, contrato, lote, cobrança, etc.)
- [ ] Documentar relacionamentos entre tabelas
- [ ] Entender as 93 tabelas vazias — são módulos desativados ou dados ausentes?
- [ ] Criar dicionário de dados em Markdown
- [ ] Preparar documentação estruturada para consumo por IA

## Etapa 4 — Integração com Claude (após Etapa 3)

- [ ] Configurar acesso do Claude à base estruturada
- [ ] Testar capacidades de consulta e análise
- [ ] Validar com o time da AMAN
- [ ] Treinamento

---

## Referência rápida — como operar o backup atual

**Novo backup completo:**
```powershell
# 1. Conectar VPN
Remove-Item C:\Users\Alan\datalake_aman\progress.txt  # opcional: reinicia do zero
cd C:\Users\Alan\datalake_aman
python backup.py
```

**Reprocessar tabela específica:**
Remover o nome da tabela do `progress.txt`, depois rodar `python backup.py`.
