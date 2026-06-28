# Relatório de Conclusão — Etapa 1
## Backup da Base Histórica San Marino

**Para:** Mário  
**De:** Alan Dias  
**Data:** junho de 2026  
**Projeto:** AMAN — Fundação de Dados

---

## Resumo executivo

A Etapa 1 do projeto foi concluída com sucesso.

Toda a base histórica da San Marino foi extraída, inventariada e armazenada no Google Drive corporativo da AMAN. O backup cobre **35 anos de dados operacionais** em **357 tabelas**, totalizando mais de **50 milhões de registros** distribuídos nas principais áreas do negócio: clientes, lotes, vendas, cobranças, contratos, financeiro e muito mais.

Os dados estão disponíveis para acesso imediato na pasta **Data Lake Aman** no Google Drive.

---

## O que foi feito

### 1. Inventário completo do banco

Identificamos e catalogamos todas as 357 tabelas do banco `sm_teste` (sistema San Marino), com contagem de registros por tabela e classificação por volume e relevância.

### 2. Exportação dos dados

Cada tabela foi exportada individualmente para o Google Drive:

| Categoria | Quantidade | Formato |
|-----------|-----------|---------|
| Tabelas com dados | 264 | Excel (.xlsx) |
| Tabelas com grande volume | 8 | CSV dividido em partes |
| Tabelas sem dados | 93 | Excel (vazio — estrutura preservada) |
| **Total** | **357** | |

### 3. Organização no Drive

Os arquivos foram organizados na seguinte estrutura dentro da pasta **Data Lake Aman**:

```
Data Lake Aman/
└── Backup San Marino — Jun 2026/
    ├── Dados/     ← 264 tabelas com dados (xlsx e csv)
    └── Vazias/    ← 93 tabelas sem dados (estrutura preservada)
```

---

## Tabelas de maior volume

As 8 tabelas com maior volume de dados foram exportadas em formato CSV, divididas em arquivos de 1 milhão de linhas cada para facilitar o manuseio:

| Tabela | Total de registros | Arquivos gerados |
|--------|--------------------|-----------------|
| tabelapreco | 22.093.029 | 23 arquivos CSV |
| lcto | 6.863.769 | 7 arquivos CSV |
| lotesvendap | 5.477.181 | 6 arquivos CSV |
| saldos | 4.488.047 | 5 arquivos CSV |
| custoarea | 2.063.028 | 3 arquivos CSV |
| spedlote | 2.056.238 | 3 arquivos CSV |
| lotesvendab | 1.938.202 | 2 arquivos CSV |
| propostavendae | 1.239.107 | 2 arquivos CSV |

---

## Principais áreas de dados disponíveis

Com base no inventário, a base cobre as seguintes áreas de negócio:

| Área | Exemplos de tabelas |
|------|-------------------|
| Clientes | cliente, clientefone, clienteende |
| Lotes e empreendimentos | lotempreend, lotesvenda, loteiptu |
| Contratos e vendas | proposta, crm, aditivopa, refcondicao |
| Cobranças e inadimplência | cobranca, titulocb, titulopagar, refatraso |
| Financeiro | lcto, saldos, repasse, repassec |
| Notas fiscais | notafiscal, nfparcela |
| RH | funcionario, dependente, diarista |
| Tabelas de preço | tabelapreco (22M registros) |
| DIMOB / obrigações acessórias | dimobibase, dimobirenda |

---

## Sobre as tabelas vazias

Das 357 tabelas, 93 não possuem dados. Isso é esperado em sistemas de gestão: módulos que existem no sistema mas que a San Marino não utiliza, ou funcionalidades ativadas mas ainda não alimentadas. A estrutura dessas tabelas foi preservada no backup para referência futura.

---

## Acesso aos dados

**Localização:** Google Drive — pasta **Data Lake Aman**

Os arquivos Excel podem ser abertos diretamente. Os arquivos CSV de tabelas grandes podem ser importados no Excel, Python, Power BI ou qualquer ferramenta de análise.

---

## Próximos passos (Etapa 2)

Com o backup concluído, a AMAN possui agora uma cópia própria e independente de toda a base histórica da San Marino.

A Etapa 2 consistirá em estruturar esses dados em uma infraestrutura de dados proprietária da AMAN, com:

- Armazenamento cloud
- Pipelines de atualização automatizados
- Estrutura organizada para análise e modelos de crédito

Entraremos em contato em breve para alinharmos o início da Etapa 2.

---

*Relatório gerado pelo projeto datalake_aman — repositório técnico disponível em github.com/alanmdias/datalake_aman*
