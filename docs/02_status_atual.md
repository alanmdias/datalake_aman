# 02 — Status Atual

## Última execução: junho de 2026

### Resultado

| Categoria | Quantidade |
|-----------|-----------|
| Total de tabelas no banco | 357 |
| Exportadas como Excel (.xlsx) | 256 |
| Exportadas como CSV (divididas) | 8 |
| Tabelas vazias (exportadas como .xlsx vazio) | 93 |

**Status geral: COMPLETO ✓**

### Tabelas exportadas como CSV (> 900k linhas)

| Tabela | Linhas | Arquivos no Drive |
|--------|--------|-------------------|
| tabelapreco | 22.093.029 | 23 partes |
| lcto | 6.863.769 | 7 partes |
| lotesvendap | 5.477.181 | 6 partes |
| saldos | 4.488.047 | 5 partes |
| custoarea | 2.063.028 | 3 partes |
| spedlote | 2.056.238 | 3 partes |
| lotesvendab | 1.938.202 | 2 partes |
| propostavendae | 1.239.107 | 2 partes |

### Localização no Drive

Pasta: **Data Lake Aman** (ID: `0AEEhSxpe_XHHUk9PVA`)
Drive organizacional: Aman Finance

### Problemas encontrados e resolvidos

| Problema | Solução |
|----------|---------|
| Schema errado (`public` em vez de `sm`) | Corrigido em `SCHEMA = "sm"` |
| OAuth scope insuficiente (`drive.file`) | Alterado para escopo completo `drive` |
| App em modo teste sem usuário autorizado | Alan adicionado como test user no GCP |
| Drive API não habilitada | Habilitada no Google Cloud Console |
| Pasta organizacional retornava 404 | Adicionado `supportsAllDrives=True` em todas as chamadas |
| Colunas datetime com timezone quebravam o Excel | Strip de timezone antes de escrever |
| Tabelas grandes estouravam memória RAM | Leitura em chunks com LIMIT/OFFSET |
| Conexão fechada entre tabelas | Reconexão automática no loop principal |
| VPN caindo durante execução | Script retomável via `progress.txt` |
