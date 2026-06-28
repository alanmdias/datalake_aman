# 06 — Decisões Técnicas

## Por que Excel e não CSV para todas as tabelas?

Excel é mais fácil de abrir e visualizar para usuários não técnicos. CSV foi reservado apenas para tabelas que excedem o limite do Excel (1.048.576 linhas). Usamos 900.000 como limiar de segurança para deixar margem.

## Por que dividir CSVs em 1 milhão de linhas?

Arquivos muito grandes são difíceis de abrir em ferramentas comuns (Excel, LibreOffice). Partes de 1M de linhas ficam entre 90-95 MB cada, que é um tamanho razoável para download e processamento.

## Por que escopo OAuth `drive` completo e não `drive.file`?

O escopo `drive.file` só permite acesso a arquivos criados pelo próprio app. A pasta de destino foi criada pela organização e compartilhada com o Alan — portanto o escopo completo é necessário.

## Por que `supportsAllDrives=True` em todas as chamadas?

A pasta alvo é um **Shared Drive** organizacional (não um Drive pessoal). Sem esse parâmetro, a API retorna 404 ao tentar acessar itens em Shared Drives.

## Por que `progress.txt` e não um banco de dados de controle?

Simplicidade. Um arquivo texto com um nome por linha é suficiente para o caso de uso: scripts de backup pontuais, não pipelines contínuos. Fácil de editar manualmente para reprocessar tabelas.

## Por que LIMIT/OFFSET para tabelas grandes e não `chunksize` do pandas?

O `pd.read_sql` com `chunksize` retorna um iterador mas ainda pode alocar memória de forma imprevisível dependendo do driver. LIMIT/OFFSET no SQL garante que apenas o chunk pedido é transferido do banco para a memória do Python.

## Por que strip de timezone nas colunas datetime?

O `openpyxl` (engine de escrita do Excel) não suporta objetos `datetime` com timezone. Colunas do tipo `timestamptz` no PostgreSQL chegam ao pandas como `DatetimeTZDtype`. A solução é `dt.tz_localize(None)` antes de escrever — remove a informação de timezone, mas preserva o valor horário (que já estava em UTC no banco).

## Por que reconectar ao PostgreSQL entre tabelas?

A exportação de tabelas grandes pode levar vários minutos. O servidor PostgreSQL pode fechar conexões ociosas por timeout, especialmente se a VPN tiver instabilidade. A reconexão automática (`if conn.closed`) evita que uma queda de conexão aborte o backup inteiro.
