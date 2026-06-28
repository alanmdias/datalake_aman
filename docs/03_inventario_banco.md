# 03 — Inventário do Banco de Dados

## Informações gerais

- **Banco:** sm_teste
- **Host:** 192.168.16.11:5432 (acesso via VPN)
- **Schema exportado:** sm
- **Total de tabelas:** 357
- **Data do inventário:** junho de 2026

O arquivo completo com contagem de linhas por tabela está em `inventario_backup.xlsx` na raiz do projeto.

## Tabelas vazias (93 tabelas)

Estas tabelas existem no banco mas não possuem dados:

admgeral, apartamento, apartamentop, apde_apagar, apde_contabilidade, apde_custo, apde_entrada, aplicacao, ativobem, ativocalculo, ativoconta, atos_notoriais, atos_notoriais_user, auxposicao, bancocheque, bancomovi, bancosaldo, boleto, boletoparcela, calccsll, calcparceiro, chavelote, classe, comarca, comodo, compromisso, contratoaplica, contratoloca, contratolocp, controle, controledoc, crm_rescisao, custoempresa, debitoloc, dimobintermep, dimobipercen, dirfbase, dirfrenda, doctodive, doctoentra, documento, empreendvenda, encargosocial, endereco, fases_rescisao, graflocacao, grupobalanco, imovelvenda, imovelvendb, juridiconot, locacaoiptu, locacaoiptupa, lotacao, lote_termo, lotesvendas, lvp_boleto, memocheque, memodupli, menu, nfse, painel, perc_desconto, percenrateio, posicaocli, proprimovenda, receita, refantecipacao, relareceber, relcheque, relcontrole, relnotificacao, relposicaolote, relrazao, relrecibo, relreconfe, relsped003, sped, sped_aplicacao, sped_areceber, sped_desconto, sped_diversareceita, sped_notas, sped_outrareceita, spedcontabil, statuspro, tiposalario, tipovinculo, topologia, tpservico, usercob, visita, visitafone, visitaobs

## Tabelas grandes (> 900k linhas) — exportadas como CSV

| Tabela | Linhas | Partes CSV |
|--------|--------|-----------|
| tabelapreco | 22.093.029 | 23 |
| lcto | 6.863.769 | 7 |
| lotesvendap | 5.477.181 | 6 |
| saldos | 4.488.047 | 5 |
| custoarea | 2.063.028 | 3 |
| spedlote | 2.056.238 | 3 |
| lotesvendab | 1.938.202 | 2 |
| propostavendae | 1.239.107 | 2 |

## Tabelas médias relevantes (Excel, > 50k linhas)

| Tabela | Linhas | Descrição provável |
|--------|--------|--------------------|
| clientefone | 54.779 | Telefones de clientes |
| cobranca | 366.838 | Cobranças |
| dimobirenda | 273.645 | Rendas DIMOB |
| titulopagar | 414.703 | Títulos a pagar |
| titulocb | 302.923 | Títulos de cobrança |
| repassec | 236.434 | Repasses |
| aditivopa | 350.207 | Aditivos de parcelas |
| loteiptupa | 258.875 | IPTU de lotes |
| repasse | 85.837 | Repasses |
| nfparcela | 65.419 | Parcelas de NF |
| notafiscal | 65.025 | Notas fiscais |
| dimobibase | 71.895 | Base DIMOB |
| crmlote | 78.944 | CRM por lote |
| crmdepto | 77.545 | CRM por departamento |
| crm | 77.470 | CRM |
| refatraso | 61.727 | Referências de atraso |
| cobrancacarsms | 62.067 | SMS de cobrança |
| crmparcela | 62.091 | Parcelas CRM |
