# Data Catalog — San Marino (schema sm)

Base de dados: `sm_teste` | Schema: `sm` | Total de tabelas: 357

> Gerado automaticamente por `etapa1_data_catalog.py`.
> Tamanhos incluem índices. Última atualização detectada via colunas de data de modificação (quando existentes).

## Resumo por tabela

| Schema | Tabela | Linhas | Tamanho | Colunas | Chave Primária | Nº FKs | Última Atualização |
| ------ | ------ | -----: | ------- | ------: | -------------- | -----: | ------------------ |
| sm | aditivo | 3.789 | 1208 kB | 45 | sequencia, lote, quadra, dataquitacao, cod_pessoa, cod_empreendimento | 0 | — |
| sm | aditivocp | 3.815 | 544 kB | 9 | quadra, dataquitacao, cod_pessoa, lote, sequencia, parcela, cod_empreendimento | 0 | — |
| sm | aditivopa | 350.207 | 50 MB | 15 | dataquitacao, sequencia, lote, cod_empreendimento, cod_pessoa, parcela, quadra, tipo | 0 | — |
| sm | admcob | 1 | 32 kB | 13 | cod_admcob | 0 | — |
| sm | admcondominio | 18 | 32 kB | 15 | cod_admcondominio | 0 | — |
| sm | admgeral | 0 | 8192 bytes | 17 | cod_admgeral | 0 | — |
| sm | ajuizada | 13 | 24 kB | 2 | cod_ajuizada | 0 | — |
| sm | ambiente | 24 | 24 kB | 2 | cod_ambiente | 0 | — |
| sm | apartamento | 0 | 8192 bytes | 10 | cod_empresa, cod_apartamento, cod_edificio | 0 | — |
| sm | apartamentop | 0 | 8192 bytes | 13 | cod_empresa, cod_apartamento, tipo, parcela, aditamento, cod_edificio | 0 | — |
| sm | apde_apagar | 0 | 8192 bytes | 9 | cod_apde_apagar, sequencia | 0 | — |
| sm | apde_contabilidade | 0 | 8192 bytes | 10 | cod_apde_contabilidade, sequencia | 0 | — |
| sm | apde_custo | 0 | 8192 bytes | 6 | cod_apde_custo, sequencia | 0 | — |
| sm | apde_entrada | 0 | 16 kB | 39 | cod_apde_entrada | 0 | — |
| sm | aplicacao | 0 | 8192 bytes | 13 | cod_tpaplicacao, cod_agencia, cod_empresa, cod_banco, conta_corrente, data_resgate, data_aplicacao | 0 | — |
| sm | arqpadrao | 5 | 24 kB | 5 | cod_arqpadrao | 0 | — |
| sm | assunto | 36 | 24 kB | 5 | cod_assunto | 1 | — |
| sm | ativobem | 0 | 16 kB | 21 | cod_agregado, cod_empresa, cod_bem | 0 | — |
| sm | ativocalculo | 0 | 8192 bytes | 14 | cod_bem, cod_empresa, tipo, mes, ano, cod_agregado | 0 | — |
| sm | ativoconta | 0 | 8192 bytes | 11 | grupo | 0 | — |
| sm | atos_notoriais | 0 | 16 kB | 23 | cod_empreendimento, cod_pessoa, quadra, lote, sequencia, contrato | 0 | — |
| sm | atos_notoriais_user | 0 | 8192 bytes | 8 | cod_empreendimento, cod_pessoa, quadra, lote, sequencia, contrato, cod_usuario_atualizacao, data_atualizacao | 0 | — |
| sm | auxposicao | 0 | 8192 bytes | 28 | lote, cod_pessoa, cod_empreendimento, quadra, tipo, sequencia, parcela | 0 | — |
| sm | bairro | 2.526 | 240 kB | 2 | cod_bairro | 0 | — |
| sm | banco | 210 | 152 kB | 52 | cod_banco, cod_empresa, conta_corrente, cod_agencia | 0 | — |
| sm | bancocheque | 0 | 8192 bytes | 8 | conta_corrente, cod_banco, cod_agencia, cod_empresa | 0 | — |
| sm | bancomovi | 0 | 8192 bytes | 12 | cod_empresa, numero_docto, conta_corrente, cod_banco, data_lancto, cod_agencia, cod_hisbanco | 0 | — |
| sm | bancosaldo | 0 | 8192 bytes | 9 | cod_empresa, cod_agencia, conta_corrente, cod_banco, mes, ano | 0 | — |
| sm | baseresumo | 181 | 88 kB | 45 | quadra, cod_empreendimento, mes, ano, cod_pessoa, lote, sequencia | 0 | — |
| sm | boleto | 0 | 16 kB | 46 | numero, cod_departamento | 0 | — |
| sm | boletoparcela | 0 | 8192 bytes | 17 | numero, seq, cod_departamento | 0 | — |
| sm | calccsll | 0 | 8192 bytes | 21 | cod_calccsll | 0 | — |
| sm | calcirpj | 768 | 176 kB | 25 | cod_calcirpj | 0 | — |
| sm | calcirpjbase | 1.503 | 208 kB | 9 | cod_calcirpjbase | 1 | — |
| sm | calcparceiro | 0 | 8192 bytes | 50 | mes, cod_parceiro, ano, cod_empreendimento | 0 | — |
| sm | cargo | 2 | 24 kB | 2 | cod_cargo | 0 | — |
| sm | carta | 2 | 32 kB | 5 | cod_carta | 0 | — |
| sm | cartorio | 3 | 32 kB | 13 | cod_cartorio | 0 | — |
| sm | cartoriofone | 2 | 24 kB | 6 | cod_cartoriofone, sequencia | 0 | — |
| sm | categoria | 7 | 24 kB | 2 | cod_categoria | 0 | — |
| sm | caucaoloc | 240 | 80 kB | 21 | cod_caucaoloc, cod_empresa | 0 | — |
| sm | centrocusto | 40 | 24 kB | 4 | cod_centrocusto | 0 | — |
| sm | chavelote | 0 | 8192 bytes | 5 | cpf, seq_lote, lote, cod_empresa | 0 | — |
| sm | chavemovto | 2 | 24 kB | 10 | hora, data_retirada, cpf, cod_empresa | 0 | — |
| sm | chaventrega | 1 | 32 kB | 28 | cpf | 0 | — |
| sm | classe | 0 | 8192 bytes | 2 | cod_classe | 0 | — |
| sm | cliente | 38.527 | 13 MB | 44 | cod_cliente | 0 | — |
| sm | clientecontab | 1.340 | 392 kB | 39 | cod_clientecontab | 0 | — |
| sm | clientecontabende | 1.348 | 408 kB | 11 | cod_endereco, cod_clientecontab | 0 | — |
| sm | clientecontabfone | 970 | 216 kB | 7 | sequencia, cod_clientecontab | 0 | — |
| sm | clienteende | 38.822 | 10200 kB | 11 | cod_endereco, cod_cliente | 0 | — |
| sm | clientefone | 54.779 | 10016 kB | 7 | cod_cliente, sequencia | 0 | — |
| sm | cobranca | 366.838 | 94 MB | 35 | cod_pessoa, sequencia | 0 | — |
| sm | cobrancacarsms | 62.067 | 6648 kB | 8 | quadra, cod_pessoa, cod_empreendimento, tipo, lote, data_envio | 0 | — |
| sm | cobrancanot | 9.014 | 1104 kB | 10 | cod_empreendimento, cod_pessoa, quadra, lote, sequencia, tipo, data_notificaocao | 0 | — |
| sm | cobrancaparc | 24.999 | 3840 kB | 15 | parcela, tipo, lote, quadra, cod_empreendimento, cod_pessoa, sequencia, ordem, data_cobranca | 0 | — |
| sm | cobrancaprop | 9.795 | 1464 kB | 17 | ordem, cod_empreendimento, data_cobranca, quadra, lote, sequencia, cod_pessoa | 0 | — |
| sm | comarca | 0 | 8192 bytes | 3 | cod_comarca | 0 | — |
| sm | comodo | 0 | 8192 bytes | 2 | cod_comodo | 0 | — |
| sm | complehistorico | 34 | 24 kB | 2 | cod_comple_historico | 0 | — |
| sm | compromisso | 0 | 16 kB | 9 | cod_compromisso | 0 | — |
| sm | comunicar | 4 | 32 kB | 15 | cod_comunicar | 0 | — |
| sm | comunicar_img | 1 | 104 kB | 5 | cod_comunicar_img | 1 | — |
| sm | comunicar_msg | 3 | 32 kB | 6 | cod_comunicar_msg, sequencia | 0 | — |
| sm | comunicar_prazo | 1 | 24 kB | 5 | cod_comunicar_prazo | 1 | 2023-09-21 |
| sm | contador | 69 | 64 kB | 19 | cod_contador | 0 | — |
| sm | contratoaltpar | 80 | 64 kB | 12 | contrato, cod_empresa, data_pedido | 0 | — |
| sm | contratoaplica | 0 | 8192 bytes | 12 | cod_tpaplicacao, data_aplicacao, cod_agencia, cod_empresa, conta_corrente, cod_banco | 0 | — |
| sm | contratoloca | 0 | 8192 bytes | 39 | cod_empresa, contrato | 0 | — |
| sm | contratolocp | 0 | 16 kB | 33 | aditamento, parcela, contrato, tipo_parcela, cod_empresa | 0 | — |
| sm | controle | 0 | 16 kB | 11 | ano, cod_controle | 0 | — |
| sm | controledoc | 0 | 8192 bytes | 5 | ano, cod_controledoc, sequencia | 0 | — |
| sm | cor | 6 | 24 kB | 2 | cod_cor | 0 | — |
| sm | corretor | 5 | 24 kB | 2 | cod_corretor | 0 | — |
| sm | crm | 77.470 | 12 MB | 14 | crm_id | 0 | — |
| sm | crm_quitacao | 417 | 128 kB | 21 | cod_crm_quitacao | 0 | — |
| sm | crm_rescisao | 0 | 8192 bytes | 5 | crm_rescisao_id | 2 | — |
| sm | crmdepto | 77.545 | 11 MB | 11 | crmdepto_id | 1 | — |
| sm | crmlote | 78.944 | 8528 kB | 6 | crm_id, cod_empreendimento, cod_pessoa, quadra, lote, sequencia | 0 | — |
| sm | crmparcela | 62.091 | 7776 kB | 8 | cod_empreendimento, cod_pessoa, quadra, lote, sequencia, tipo, parcela, crm_id | 0 | — |
| sm | ctaempreend | 291 | 88 kB | 23 | ind_1e2p, cod_empreendimento, sequencia | 0 | — |
| sm | ctareflexo | 451 | 112 kB | 8 | cod_empresa, conta_grau | 0 | — |
| sm | ctareflexo_novo | 712 | 136 kB | 10 | cod_empresa, conta_reduzida | 0 | — |
| sm | ctarepasse | 244 | 64 kB | 23 | ind_1e2p, cod_empreendimento, sequencia | 0 | — |
| sm | custoarea | 2.063.028 | 319 MB | 29 | cod_pessoa, quadra, lote, cod_empreendimento, ano, mes | 0 | — |
| sm | custoarear | 5.451 | 816 kB | 13 | mes, cod_empreendimento, ano | 0 | — |
| sm | custoempresa | 0 | 16 kB | 17 | numero, cod_empreendimento, sequencia, parcela, cod_pessoa, cod_empresa, tipo | 0 | — |
| sm | dados_api | 1 | 24 kB | 5 | cod_banco, cod_agencia, conta_corrente | 0 | — |
| sm | darfcofins | 2.816 | 568 kB | 18 | cod_darfcofins | 0 | — |
| sm | darfpis | 2.860 | 496 kB | 14 | cod_darfpis | 0 | — |
| sm | debitoloc | 0 | 8192 bytes | 18 | tipo, documento, aditamento, contrato, cod_empresa, parcela, cod_hislocacao | 0 | — |
| sm | departamento | 15 | 24 kB | 2 | cod_departamento | 0 | — |
| sm | dependente | 521 | 120 kB | 11 | sequencia, cod_empresa, cod_funcionario | 0 | — |
| sm | diarista | 17.278 | 3144 kB | 24 | cod_apartamento, cod_edificio, tipo_servico, cod_empresa, data_inicio | 0 | — |
| sm | diaristab | 23.851 | 3072 kB | 10 | cod_hisrateio, cod_apartamento, data_inicio, cod_edificio, tipo_servico, cod_empresa | 0 | — |
| sm | dimobibase | 71.895 | 20 MB | 25 | quadra_cliente, ano, sequencia, tipo, cod_divisao, cod_empreendimento, cod_empresa, lote | 0 | — |
| sm | dimobintermed | 1 | 32 kB | 21 | cod_empreendimento, data_movimento, cod_empresa_parceira, cod_empresa | 0 | — |
| sm | dimobintermep | 0 | 8192 bytes | 13 | cod_empresa_parceira, cod_empresa, lote, cod_pessoa, data_movimento, quadra, cod_empreendimento, sequencia | 0 | — |
| sm | dimobipercen | 0 | 8192 bytes | 6 | sequencia, cod_empreendimento | 0 | — |
| sm | dimobirenda | 273.645 | 35 MB | 12 | sequencia, tipo, lote, quadra_cliente, cod_empresa, cod_empreendimento, mes, cod_divisao, ano | 0 | — |
| sm | dirfbase | 0 | 8192 bytes | 12 | cod_empresa, cod_dirfbase_rf, ano, cnpj_cpf, tipo, cod_funcionario | 0 | — |
| sm | dirfrenda | 0 | 8192 bytes | 27 | cod_funcionario, cod_empresa, mes, cod_dirfrenda_rf, ano, tipo, cnpj_cpf | 0 | — |
| sm | doctodive | 0 | 8192 bytes | 33 | nota_fiscal, tipo, cod_pessoa, ordem, tipo_arquivo | 0 | — |
| sm | doctoentra | 0 | 16 kB | 38 | cod_pessoa, nota_fiscal, tipo | 0 | — |
| sm | documento | 0 | 8192 bytes | 4 | sequencia, cod_documento | 0 | — |
| sm | edificio | 48 | 32 kB | 12 | cod_edificio | 0 | — |
| sm | empreendimento | 173 | 112 kB | 75 | cod_empreendimento | 0 | — |
| sm | empreendimento_empresas_termo | 352 | 56 kB | 4 | cod_empreendimento, sequencia | 1 | — |
| sm | empreendimentocta | 2.518 | 408 kB | 8 | conta_reduzida, sequencia, cod_empreendimento | 0 | — |
| sm | empreendvenda | 0 | 8192 bytes | 2 | cod_empreendvenda | 0 | — |
| sm | empresa | 269 | 160 kB | 69 | cod_empresa | 0 | — |
| sm | empresa_paramcsll | 60 | 24 kB | 2 | cod_empresa, cod_param_csll | 0 | — |
| sm | empresa_paramirpj | 172 | 24 kB | 2 | cod_empresa, cod_param_irpj | 0 | — |
| sm | empresacta | 2.166 | 424 kB | 20 | sequencia, cod_empresa | 0 | — |
| sm | encargosocial | 0 | 8192 bytes | 13 | cod_receita, sequencia, cod_empresa, data_emissao | 0 | — |
| sm | endereco | 0 | 8192 bytes | 9 | cod_endereco | 0 | — |
| sm | envio_notificacao | 10.995 | 2440 kB | 27 | cod_envio_notificacao | 0 | — |
| sm | envio_notificacaoalt | 2.635 | 432 kB | 11 | cod_envio_notificacaoalt | 1 | — |
| sm | estado | 27 | 24 kB | 6 | cod_estado | 0 | — |
| sm | estadocivil | 7 | 24 kB | 2 | cod_estadocivil | 0 | — |
| sm | etiqueta | 1 | 32 kB | 8 | cod_etiqueta, quadra, lote | 0 | — |
| sm | exigibilidade | 7 | 24 kB | 2 | cod_exigibilidade | 0 | — |
| sm | fases_rescisao | 0 | 8192 bytes | 2 | fases_rescisao_id | 0 | — |
| sm | fiador | 3.739 | 1136 kB | 40 | cod_empresa, cod_fiador | 0 | — |
| sm | fiadorende | 3.544 | 1072 kB | 12 | cod_empresa, cod_fiador, cod_endereco | 0 | — |
| sm | fiadorfone | 3.130 | 688 kB | 8 | sequencia, cod_fiador, cod_empresa | 0 | — |
| sm | filtrocli | 5.628 | 592 kB | 12 | lote, cod_empreendimento, sequencia, quadra, cod_cliente | 0 | — |
| sm | forma_pagamento | 8 | 24 kB | 2 | cod_forma_pagamento | 0 | — |
| sm | fornecedor | 9.140 | 2912 kB | 40 | cod_fornecedor | 0 | — |
| sm | fornecedorende | 9.094 | 2424 kB | 11 | cod_fornecedor, cod_endereco | 0 | — |
| sm | fornecedorfone | 6.279 | 1096 kB | 7 | sequencia, cod_fornecedor | 0 | — |
| sm | funcao | 62 | 24 kB | 13 | cod_funcao | 0 | — |
| sm | funcionadoc | 629 | 136 kB | 39 | cod_empresa, cod_funcionario | 0 | — |
| sm | funcionaemp | 100 | 72 kB | 92 | cod_funcionario, cod_empresa | 0 | — |
| sm | funcionario | 230 | 72 kB | 43 | cod_empresa, cod_funcionario | 0 | — |
| sm | graflocacao | 0 | 8192 bytes | 3 | cod_graflocacao | 0 | — |
| sm | grupobalanco | 0 | 8192 bytes | 2 | cod_grupobalanco | 0 | — |
| sm | helpdesk | 680 | 360 kB | 17 | cod_helpdesk | 0 | — |
| sm | helpdesk_img | 132 | 28 MB | 3 | cod_helpdesk_img | 1 | — |
| sm | hisbanco | 237 | 64 kB | 4 | cod_hisbanco | 0 | — |
| sm | hislocacao | 129 | 56 kB | 10 | cod_hislocacao, cod_empresa | 0 | — |
| sm | hispadrao | 420 | 88 kB | 2 | cod_hispadrao | 0 | — |
| sm | hisrateio | 45 | 24 kB | 5 | cod_hisrateio | 0 | — |
| sm | honorarioadv | 1.792 | 248 kB | 17 | mes, cod_empreendimento, cod_pessoa, dia_sequencia, cod_empresa, ano | 0 | — |
| sm | honorariopar | 24.651 | 3056 kB | 14 | mes, dia_sequencia, cod_empresa, cod_empreendimento, cod_pessoa, sequencia, ano | 0 | — |
| sm | imovel | 3.591 | 792 kB | 61 | cod_imovel, cod_empresa | 0 | — |
| sm | imoveldep | 1.571 | 264 kB | 12 | tipo, cod_pessoa, cod_parceiro, cod_imov_contrato, cod_empresa | 0 | — |
| sm | imovelficha | 18.936 | 1592 kB | 4 | cod_imovel, cod_ambiente, cod_empresa | 0 | — |
| sm | imovelimg | 3 | 160 kB | 5 | cod_imagem, cod_imovel, cod_empresa | 0 | — |
| sm | imovelkit | 23 | 24 kB | 2 | cod_imovelkit | 0 | — |
| sm | imovelvenda | 0 | 16 kB | 123 | cod_imovelvenda | 0 | — |
| sm | imovelvendb | 0 | 8192 bytes | 7 | cod_imovelvendb, sequencia | 0 | — |
| sm | inadimplencia | 2.936 | 576 kB | 13 | quadra, cod_empreendimento, cod_cliente, lote, sequencia | 0 | — |
| sm | indadmissao | 3 | 24 kB | 2 | cod_indadmissao | 0 | — |
| sm | indice | 296 | 80 kB | 17 | ano, cod_indice, mes | 0 | — |
| sm | indicecalc | 511 | 120 kB | 16 | cod_indicecalc, data_indice | 0 | — |
| sm | indicepreco | 108 | 24 kB | 4 | cod_indicepreco, parcela | 0 | — |
| sm | instrucao | 11 | 24 kB | 2 | cod_instrucao | 0 | — |
| sm | iof_aplicacao | 30 | 24 kB | 2 | dia | 0 | — |
| sm | irrf_aplicacao | 4 | 24 kB | 3 | dia_inicial, dia_final | 0 | — |
| sm | juridiconot | 0 | 8192 bytes | 9 | cod_empreendimento, cod_pessoa, quadra, lote, sequencia, tipo, data_notificaocao | 0 | — |
| sm | lancamentos | 609 | 184 kB | 14 | tipo, data_lcto, numero, cod_empresa, sequencia | 0 | — |
| sm | lcto | 6.863.769 | 1321 MB | 21 | tipo, cod_empresa, numero, data_lcto, sequencia | 0 | — |
| sm | locacaoiptu | 0 | 16 kB | 14 | cod_empresa, cod_filial, tipo, ano, cod_imovel | 0 | — |
| sm | locacaoiptupa | 0 | 8192 bytes | 20 | cod_filial, parcela, ano, cod_imovel, tipo, cod_empresa | 0 | — |
| sm | locacaolib | 231 | 80 kB | 31 | cod_locacaolib | 0 | — |
| sm | locacaolibc | 444 | 88 kB | 4 | parcela, cod_locacaolib | 0 | — |
| sm | locacaolibp | 517 | 112 kB | 16 | cod_locacaolib, sequencia | 0 | — |
| sm | locador | 1.717 | 632 kB | 43 | cod_empresa, cod_locador | 0 | — |
| sm | locadorende | 1.649 | 544 kB | 12 | cod_locador, cod_empresa, cod_endereco | 0 | — |
| sm | locadorfone | 2.682 | 576 kB | 8 | sequencia, cod_empresa, cod_locador | 0 | — |
| sm | locadorpool | 541 | 176 kB | 39 | cod_locadorpool | 0 | — |
| sm | locadorpoolende | 541 | 152 kB | 11 | cod_endereco, cod_locadorpool | 0 | — |
| sm | locadorpoolfone | 546 | 144 kB | 7 | cod_locadorpool, sequencia | 0 | — |
| sm | locatario | 4.048 | 1320 kB | 40 | cod_empresa, cod_locatario | 0 | — |
| sm | locatarioende | 3.853 | 1208 kB | 12 | cod_endereco, cod_locatario, cod_empresa | 0 | — |
| sm | locatariofone | 5.267 | 600 kB | 8 | sequencia, cod_empresa, cod_locatario | 0 | — |
| sm | locatariopool | 2.281 | 328 kB | 39 | cod_locatariopool | 0 | — |
| sm | locatariopoolende | 2.281 | 256 kB | 11 | cod_locatariopool, cod_endereco | 0 | — |
| sm | locatariopoolfone | 602 | 104 kB | 7 | sequencia, cod_locatariopool | 0 | — |
| sm | logradouro | 14 | 24 kB | 2 | cod_logradouro | 0 | — |
| sm | lotacao | 0 | 8192 bytes | 2 | cod_lotacao | 0 | — |
| sm | lote_termo | 0 | 8192 bytes | 8 | data_emissao, sequencia, lote, quadra, cod_pessoa, cod_empreendimento | 0 | — |
| sm | loteiptu | 36.073 | 4704 kB | 18 | cod_empreendimento, cod_empresa, tipo, quadra, ano, lote | 0 | — |
| sm | loteiptupa | 258.875 | 42 MB | 18 | quadra, parcela, cod_empreendimento, cod_empresa, ano, lote, tipo | 0 | — |
| sm | lotempreend | 49.670 | 8272 kB | 43 | cod_empreendimento, lote, quadra, sequencia | 0 | — |
| sm | lotempreend_termo | 2.037 | 280 kB | 16 | cod_empreendimento, quadra, lote, sequencia, cod_pessoa, data_emissao | 0 | — |
| sm | lotesvenda | 45.489 | 11 MB | 47 | lote, sequencia, cod_empreendimento, cod_pessoa, quadra | 0 | — |
| sm | lotesvenda_fornecedor | 248 | 72 kB | 6 | cod_empreendimento, cod_pessoa, quadra, lote, sequencia, cod_fornecedor | 0 | — |
| sm | lotesvenda_obs | 32.538 | 5360 kB | 10 | cod_empreendimento, cod_pessoa, quadra, lote, sequencia, ordem | 0 | — |
| sm | lotesvenda_parc | 1.205 | 176 kB | 7 | cod_empreendimento, cod_pessoa, quadra, lote, sequencia, cod_parceiro | 0 | — |
| sm | lotesvendab | 1.938.202 | 282 MB | 20 | cod_empreendimento, parcela, lote, tipo, cod_pessoa, sequencia, seq_pagtos, quadra | 0 | — |
| sm | lotesvendap | 5.477.181 | 2007 MB | 46 | quadra, sequencia, parcela, cod_empreendimento, lote, tipo, cod_pessoa | 0 | — |
| sm | lotesvendap_descricao | 22.246 | 3848 kB | 8 | cod_empreendimento, cod_pessoa, quadra, lote, sequencia, tipo, parcela | 0 | — |
| sm | lotesvendas | 0 | 8192 bytes | 9 | cod_pessoa, lote, cod_empreendimento, sequencia, quadra, cod_statuscc, data_status | 0 | — |
| sm | lvp_boleto | 0 | 16 kB | 20 | cod_empreendimento, cod_pessoa, quadra, lote, sequencia, tipo, parcela, data_geracao, nosso_numero, seu_numero | 0 | — |
| sm | mapas | 1 | 1848 kB | 2 | cod_empreendimento | 0 | — |
| sm | memocancelado | 5.877 | 656 kB | 7 | cod_memocancelado | 0 | — |
| sm | memocheque | 0 | 8192 bytes | 21 | sequencia, numero, cod_empresa | 0 | — |
| sm | memodupli | 0 | 8192 bytes | 8 | parcela, duplicata, numero, cod_empresa, tipo_titulo, cod_pessoa | 0 | — |
| sm | memorial | 10.815 | 9248 kB | 4 | cod_empreendimento, quadra, lote | 0 | — |
| sm | menu | 0 | 16 kB | 6 | cod_menu | 0 | — |
| sm | midia | 4 | 24 kB | 2 | cod_midia | 0 | — |
| sm | msgboleto | 12 | 24 kB | 2 | cod_msgboleto | 0 | — |
| sm | municipio | 5.567 | 496 kB | 4 | cod_municipio | 0 | — |
| sm | nacionalidade | 25 | 24 kB | 2 | cod_nacionalidade | 0 | — |
| sm | nf_auxiliar | 531 | 336 kB | 42 | cod_nf_auxiliar | 0 | — |
| sm | nfp_auxiliar | 518 | 128 kB | 14 | cod_nfp_auxiliar | 1 | — |
| sm | nfparcela | 65.419 | 8328 kB | 12 | parcela, cod_empresa, numero | 0 | — |
| sm | nfse | 0 | 16 kB | 30 | cod_nfse | 0 | — |
| sm | notafiscal | 65.025 | 22 MB | 41 | cod_empresa, numero | 0 | — |
| sm | notafiscaltipo | 4 | 24 kB | 15 | cod_tipo | 0 | — |
| sm | notificacao | 71 | 64 kB | 35 | cod_notificacao, ano | 0 | — |
| sm | notificacaodesp | 12 | 24 kB | 5 | cod_notificacao, ano, data_despesa | 0 | — |
| sm | notificacaoeql | 117 | 24 kB | 5 | quadra, lote, ano, cod_empreendimento, cod_notificacao | 0 | — |
| sm | notificacaomd | 161 | 56 kB | 5 | data_md, cod_notificacaomd, ano_md, cod_tpnotificacao | 0 | — |
| sm | notificacaoprop | 66 | 64 kB | 8 | ano, cod_notificacao, data_proposta | 0 | — |
| sm | numeracaoap | 6 | 24 kB | 2 | tipo | 0 | — |
| sm | numeracaoboleto | 3 | 24 kB | 2 | departamento | 0 | — |
| sm | ocorrencia | 584 | 136 kB | 4 | cod_ocorrencia | 1 | — |
| sm | ocorrencia_img | 32 | 7760 kB | 3 | cod_ocorrencia_img | 1 | — |
| sm | painel | 0 | 8192 bytes | 2 | cod_painel | 0 | — |
| sm | pais | 244 | 56 kB | 2 | cod_pais | 0 | — |
| sm | param_csll | 1 | 24 kB | 13 | cod_param_csll | 0 | 2020-05-23 |
| sm | param_irpj | 1 | 24 kB | 15 | cod_param_irpj | 0 | 2025-06-18 |
| sm | parametro_nfse | 2 | 32 kB | 24 | cod_empresa | 0 | — |
| sm | parentesco | 3 | 24 kB | 2 | cod_parentesco | 0 | — |
| sm | pedido_alteracao_valor_aluguel | 2 | 120 kB | 23 | cod_pedido_alteracao_valor_aluguel | 0 | 2026-06-02 |
| sm | perc_desconto | 0 | 8192 bytes | 4 | cod_empreendimento, sequencia | 0 | — |
| sm | percenrateio | 0 | 8192 bytes | 3 | cod_empresa, cod_pessoa | 0 | — |
| sm | planoconta | 12.724 | 1944 kB | 7 | tipo_conta, cod_empresa, numero | 0 | — |
| sm | planoconta_tipo | 1.089 | 152 kB | 6 | cod_empresa, tipo_conta, numero, sequencia | 0 | — |
| sm | posicaocli | 0 | 8192 bytes | 10 | lote, quadra, cod_empreendimento, cod_cliente, sequencia | 0 | — |
| sm | processo | 38 | 32 kB | 25 | cod_processo | 0 | — |
| sm | processoprop | 1 | 32 kB | 8 | cod_processo, ano, data_proposta | 0 | — |
| sm | programador | 2 | 24 kB | 2 | cod_programador | 0 | — |
| sm | proposta | 12.094 | 2040 kB | 28 | cod_proposta | 2 | — |
| sm | proposta_condicao | 26.391 | 2840 kB | 10 | cod_proposta, sequencia | 1 | — |
| sm | proposta_parceiro | 1.246 | 144 kB | 4 | cod_proposta, cod_parceiro | 0 | — |
| sm | proposta_seq | 1.427 | 168 kB | 5 | cod_proposta, cod_pessoa, seq_lote | 0 | — |
| sm | propostaobco | 1 | 32 kB | 3 | cod_propostaobco | 0 | — |
| sm | propostavenda | 23.840 | 4256 kB | 29 | cod_propostavenda, sequencia | 0 | — |
| sm | propostavendae | 1.239.107 | 118 MB | 10 | parcela, cod_propostavendae, tipo, sequencia | 0 | — |
| sm | propostavendap | 3.341 | 416 kB | 5 | cod_pessoa, sequencia, cod_propostavendap | 0 | — |
| sm | proprimovenda | 0 | 16 kB | 20 | cod_proprimovenda, seq_proprimovenda | 0 | — |
| sm | protocolo | 1 | 24 kB | 2 | departamento_id | 0 | — |
| sm | raca | 6 | 24 kB | 2 | cod_raca | 0 | — |
| sm | rateioperc | 21 | 24 kB | 5 | cod_pessoa, cod_empresa | 0 | — |
| sm | rateiopool | 23.064 | 3056 kB | 20 | cod_pessoa, cod_empresa, data_rateio | 0 | — |
| sm | receita | 0 | 8192 bytes | 12 | sequencia, cod_empresa | 0 | — |
| sm | refantecipacao | 0 | 8192 bytes | 7 | cod_ refantecipacao, cod_tpparcela, parcela | 0 | — |
| sm | refatraso | 61.727 | 7304 kB | 11 | cod_refatraso | 1 | — |
| sm | refcondicao | 22.101 | 2424 kB | 12 | cod_refcondicao | 1 | — |
| sm | refentrada | 7.992 | 768 kB | 7 | cod_refentrada | 1 | — |
| sm | refinanciamento | 8.017 | 2272 kB | 52 | cod_refinanciamento | 1 | — |
| sm | refopcao | 6 | 24 kB | 2 | cod_refopcao | 0 | — |
| sm | refvlrpresente | 8.015 | 992 kB | 9 | cod_refvlrpresente | 1 | — |
| sm | regime | 1 | 24 kB | 2 | cod_regime | 0 | — |
| sm | regime_tributario | 6 | 24 kB | 2 | cod_regime_tributario | 0 | — |
| sm | regimecasamento | 6 | 24 kB | 2 | cod_regimecasamento | 0 | — |
| sm | regimeprevidencia | 2 | 24 kB | 2 | cod_regimeprevidencia | 0 | — |
| sm | regimetrabalho | 2 | 24 kB | 2 | cod_regimetrabalho | 0 | — |
| sm | regularizada | 7 | 24 kB | 2 | cod_regularizada | 0 | — |
| sm | relap | 11 | 32 kB | 34 | data_vencimento, cod_pessoa, tipo, nota_fiscal, ordem, seq | 0 | — |
| sm | relareceber | 0 | 8192 bytes | 32 | tipo, cod_empreendimento, cod_pessoa, lote, quadra, sequencia, parcela | 0 | — |
| sm | relboleto | 1 | 32 kB | 59 | cod_departamento, numero | 0 | — |
| sm | relcheque | 0 | 8192 bytes | 8 | numero | 0 | — |
| sm | relcontrole | 0 | 16 kB | 14 | rsequencia, rcod_controle, rano | 0 | — |
| sm | relextrato | 15 | 24 kB | 18 | quadra, tipo, sequencia, parcela, cod_empreendimento, cod_pessoa, lote | 0 | — |
| sm | relmemorando | 1 | 32 kB | 14 | cod_empresa, numero, sequencia | 0 | — |
| sm | relmovbco | 12 | 24 kB | 16 | cod_historico, cod_agencia, conta, numero, data_lancto, cod_banco, cod_empresa | 0 | — |
| sm | relnotificacao | 0 | 8192 bytes | 9 | rano, rcod_notificacao | 0 | — |
| sm | relparcboleto | 8 | 24 kB | 18 | cod_departamento, numero, sequencia | 0 | — |
| sm | relposicaolote | 0 | 8192 bytes | 15 | cod_empreendimento, lote, sequencia, quadra, cod_pessoa | 0 | — |
| sm | relqdresumo | 1 | 32 kB | 66 | cod_fc, cod_locatario, contrato, cod_locador, cod_empresa | 0 | — |
| sm | relquitacao | 25 | 24 kB | 16 | parcela, cod_pessoa, cod_empreendimento, tipo, sequencia, quadra, lote, cod_empresa | 0 | — |
| sm | relrazao | 0 | 8192 bytes | 14 | conta_reduzida, tipo, numero, sequencia, conta_analitica, data_lancamento | 0 | — |
| sm | relrecibo | 0 | 16 kB | 37 | cod_locador, parcela, cod_empresa, contrato | 0 | — |
| sm | relreconfe | 0 | 8192 bytes | 15 | cod_empresa, contrato, cod_imovel | 0 | — |
| sm | relrecresumo | 3 | 24 kB | 12 | periodo, recpor, cod_empreendimento | 0 | — |
| sm | relsped003 | 0 | 8192 bytes | 14 | trl_dia, trl_tipr, trl_mes, trl_ano, trl_sequ, trl_dbcr, trl_tipo, trl_nula | 0 | — |
| sm | relsped030 | 16 | 24 kB | 8 | trm_nula, trm_tipo, trm_tipr, trm_dia, trm_ano, trm_mes | 0 | — |
| sm | reltabela | 97 | 64 kB | 22 | quadra, lote, cod_empreendimento | 0 | — |
| sm | remessa | 36.850 | 4296 kB | 7 | cod_empresa, cod_empreendimento, cod_banco, cod_agencia, conta_corrente, data_remessa | 0 | — |
| sm | remessam | 3.496 | 480 kB | 8 | cod_empresa, cod_empreendimento, cod_banco, cod_agencia, conta_corrente, mes, ano | 0 | — |
| sm | repasse | 85.837 | 17 MB | 23 | cod_empresa, parcela, tipo_parcela, contrato, aditamento, cod_pessoa | 0 | — |
| sm | repassec | 236.434 | 29 MB | 11 | cod_hislocacao, contrato, cod_empresa, tipo_parcela, parcela, cod_pessoa, aditamento | 0 | — |
| sm | representante | 329 | 112 kB | 17 | cod_representante | 0 | — |
| sm | requerente | 40 | 24 kB | 5 | sequencia, cod_requerente | 0 | — |
| sm | requerido | 51 | 24 kB | 5 | sequencia, cod_requerido | 0 | — |
| sm | reservado | 1 | 24 kB | 2 | cod_reservado | 0 | — |
| sm | responsavel | 1 | 32 kB | 21 | cod_responsavel | 0 | — |
| sm | resultadonot | 16 | 24 kB | 2 | cod_resultadonot | 0 | — |
| sm | rt_especial | 12 | 24 kB | 2 | cod_rt_especial | 0 | — |
| sm | saldos | 4.488.047 | 654 MB | 11 | cod_empresa, mes, ano, conta_analitica, tipo | 0 | — |
| sm | situacao | 28 | 24 kB | 2 | cod_situacao | 0 | — |
| sm | socios | 1.205 | 184 kB | 11 | cod_socio, cod_empresa, ano | 0 | — |
| sm | solicita | 8 | 24 kB | 4 | solicita_id | 0 | — |
| sm | sped | 0 | 8192 bytes | 9 | cod_sped | 0 | — |
| sm | sped_aplicacao | 0 | 8192 bytes | 10 | cod_sped_aplicacao | 1 | — |
| sm | sped_areceber | 0 | 8192 bytes | 16 | cod_sped_areceber | 1 | — |
| sm | sped_desconto | 0 | 8192 bytes | 9 | cod_sped_desconto | 1 | — |
| sm | sped_diversareceita | 0 | 8192 bytes | 9 | cod_sped_diversareceita | 1 | — |
| sm | sped_notas | 0 | 8192 bytes | 17 | cod_sped_notas | 1 | — |
| sm | sped_outrareceita | 0 | 8192 bytes | 9 | cod_sped_outrareceita | 1 | — |
| sm | spedcontabil | 0 | 16 kB | 5 | sequencia, regis, ordem, cod_empresa | 0 | — |
| sm | spedctaparam | 142 | 64 kB | 28 | cod_empresa | 0 | — |
| sm | spedlote | 2.056.238 | 422 MB | 19 | cod_pessoa, lote_sequencia, sigla_cst, cod_empreend_nfiscal_agencia, quadra_banco, ano, cod_empresa, mes | 0 | — |
| sm | spedtrimestre | 1.755 | 248 kB | 12 | cod_empresa, ano, trimestre | 0 | — |
| sm | status_crm | 3 | 24 kB | 2 | statuscrm_id | 0 | — |
| sm | status_helpdesk | 5 | 24 kB | 2 | cod_status_helpdesk | 0 | — |
| sm | status_proposta | 4 | 24 kB | 2 | cod_status_proposta | 0 | — |
| sm | statuscc | 1 | 24 kB | 2 | cod_statuscc | 0 | — |
| sm | statuscli | 1 | 24 kB | 2 | cod_statuscli | 0 | — |
| sm | statuscob | 15 | 24 kB | 2 | cod_statuscob | 0 | — |
| sm | statusnot | 29 | 24 kB | 2 | cod_statusnot | 0 | — |
| sm | statuspro | 0 | 8192 bytes | 2 | cod_statuspro | 0 | — |
| sm | subtipogasto | 217 | 56 kB | 2 | cod_subtipogasto | 0 | — |
| sm | suporte | 1 | 32 kB | 12 | cod_suporte | 0 | — |
| sm | tabelainss | 730 | 104 kB | 5 | ano_inss, mes_inss, sequencia_inss | 0 | — |
| sm | tabelairrf | 1.074 | 136 kB | 6 | sequencia_irrf, mes_irrf, ano_irrf | 0 | — |
| sm | tabelairrfinss | 218 | 64 kB | 14 | mes_tabela, ano_tabela | 0 | — |
| sm | tabelapreco | 22.093.029 | 3535 MB | 21 | cod_indicepreco, cod_empreendimento, quadra, mes, lote, ano, parcela | 0 | — |
| sm | taxajuros | 4.404 | 336 kB | 2 | data | 0 | — |
| sm | tipo_atendimento | 3 | 24 kB | 3 | cod_tipo_atendimento | 0 | — |
| sm | tipo_contrato | 3 | 24 kB | 2 | cod_tipo_contrato | 0 | — |
| sm | tipo_termo | 7 | 24 kB | 2 | cod_tipo_termo | 0 | — |
| sm | tipo_tributacao | 9 | 24 kB | 2 | cod_tipotributacao | 0 | — |
| sm | tipoadmissao | 5 | 24 kB | 2 | cod_tipoadmissao | 0 | — |
| sm | tipodcontab | 15 | 24 kB | 2 | cod_tipodcontab | 0 | — |
| sm | tipodistrato | 5 | 24 kB | 2 | cod_tipodistrato | 0 | — |
| sm | tipoempcta | 49 | 24 kB | 2 | cod_tipoempcta | 0 | — |
| sm | tipoempreendcta | 29 | 24 kB | 2 | cod_tipoempreendcta | 0 | — |
| sm | tipogasto | 44 | 24 kB | 2 | cod_tipogasto | 0 | — |
| sm | tipolancto | 28 | 24 kB | 2 | cod_tipolancto | 0 | — |
| sm | tipoliquida | 5 | 24 kB | 2 | cod_tipoliquida | 0 | — |
| sm | tipopgto | 23 | 24 kB | 6 | cod_tipopgto | 0 | — |
| sm | tiposalario | 0 | 8192 bytes | 2 | cod_tiposalario | 0 | — |
| sm | tipovinculo | 0 | 8192 bytes | 2 | cod_tipovinculo | 0 | — |
| sm | titulocb | 302.923 | 48 MB | 12 | numero, sequencia, cod_empresa, parcela, cod_pessoa, tipo | 0 | — |
| sm | titulopagar | 414.703 | 98 MB | 34 | tipo, parcela, cod_empresa, cod_pessoa, numero | 0 | — |
| sm | topologia | 0 | 8192 bytes | 2 | cod_topologia | 0 | — |
| sm | tpaplicacao | 7 | 24 kB | 17 | cod_tpaplicacao | 0 | — |
| sm | tplocacao | 10 | 24 kB | 2 | cod_tplocacao | 0 | — |
| sm | tpnotificacao | 11 | 24 kB | 2 | cod_tpnotificacao | 0 | — |
| sm | tpparcela | 11 | 24 kB | 2 | cod_tpparcela | 0 | — |
| sm | tpresidencia | 2 | 24 kB | 2 | cod_tpresidencia | 0 | — |
| sm | tpservico | 0 | 8192 bytes | 2 | cod_tpservico | 0 | — |
| sm | tributo | 2 | 24 kB | 20 | cod_tributo | 0 | — |
| sm | usercob | 0 | 8192 bytes | 3 | idusuario, cod_empreendimento | 0 | — |
| sm | usuario | 77 | 56 kB | 20 | idusuario | 0 | — |
| sm | usuario_funcionario_depto | 26 | 24 kB | 4 | idUsuario, idEmpresa, idFuncionario, idDepartamento | 0 | — |
| sm | vendaresumo | 1.200 | 208 kB | 19 | quadra, lote, mes, tipo_acumulador, cod_empreendimento, tipo_parcela, sequencia, cod_pessoa, ano | 0 | — |
| sm | vinculo | 2 | 24 kB | 2 | cod_vinculo | 0 | — |
| sm | visita | 0 | 16 kB | 23 | cod_filial, cod_visita | 0 | — |
| sm | visitafone | 0 | 8192 bytes | 6 | sequencia, cod_filial, cod_visita | 0 | — |
| sm | visitaobs | 0 | 16 kB | 8 | cod_visitaobs, cod_filial, sequencia | 0 | — |

---

## Legenda

- **Linhas**: contagem exata via `COUNT(*)`
- **Tamanho**: `pg_total_relation_size` (dados + índices + TOAST)
- **Chave Primária**: coluna(s) que compõem a PK, conforme `information_schema`
- **Nº FKs**: quantidade de foreign keys declaradas na tabela
- **Última Atualização**: MAX de coluna de data de modificação quando identificada

## Tabelas com maior volume

| Tabela | Linhas | Tamanho |
| ------ | -----: | ------- |
| tabelapreco | 22.093.029 | 3535 MB |
| lcto | 6.863.769 | 1321 MB |
| lotesvendap | 5.477.181 | 2007 MB |
| saldos | 4.488.047 | 654 MB |
| custoarea | 2.063.028 | 319 MB |
| spedlote | 2.056.238 | 422 MB |
| lotesvendab | 1.938.202 | 282 MB |
| propostavendae | 1.239.107 | 118 MB |
| titulopagar | 414.703 | 98 MB |
| cobranca | 366.838 | 94 MB |

## Tabelas vazias (0 linhas)

`admgeral`, `apartamento`, `apartamentop`, `apde_apagar`, `apde_contabilidade`, `apde_custo`, `apde_entrada`, `aplicacao`, `ativobem`, `ativocalculo`, `ativoconta`, `atos_notoriais`, `atos_notoriais_user`, `auxposicao`, `bancocheque`, `bancomovi`, `bancosaldo`, `boleto`, `boletoparcela`, `calccsll`, `calcparceiro`, `chavelote`, `classe`, `comarca`, `comodo`, `compromisso`, `contratoaplica`, `contratoloca`, `contratolocp`, `controle`, `controledoc`, `crm_rescisao`, `custoempresa`, `debitoloc`, `dimobintermep`, `dimobipercen`, `dirfbase`, `dirfrenda`, `doctodive`, `doctoentra`, `documento`, `empreendvenda`, `encargosocial`, `endereco`, `fases_rescisao`, `graflocacao`, `grupobalanco`, `imovelvenda`, `imovelvendb`, `juridiconot`, `locacaoiptu`, `locacaoiptupa`, `lotacao`, `lote_termo`, `lotesvendas`, `lvp_boleto`, `memocheque`, `memodupli`, `menu`, `nfse`, `painel`, `perc_desconto`, `percenrateio`, `posicaocli`, `proprimovenda`, `receita`, `refantecipacao`, `relareceber`, `relcheque`, `relcontrole`, `relnotificacao`, `relposicaolote`, `relrazao`, `relrecibo`, `relreconfe`, `relsped003`, `sped`, `sped_aplicacao`, `sped_areceber`, `sped_desconto`, `sped_diversareceita`, `sped_notas`, `sped_outrareceita`, `spedcontabil`, `statuspro`, `tiposalario`, `tipovinculo`, `topologia`, `tpservico`, `usercob`, `visita`, `visitafone`, `visitaobs`
