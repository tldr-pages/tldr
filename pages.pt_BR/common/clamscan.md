# clamscan

> Um antivírus de linha de comando.
> Mais informações: <https://docs.clamav.net/manual/Usage/Scanning.html#clamscan>.

- Faz uma varredura em um arquivo por vulnerabilidades:

`clamscan {{caminho/para/arquivo}}`

- Faz uma varredura em todos os arquivos recursivamente em um diretório específico:

`clamscan -r {{caminho/para/diretório}}`

- Faz uma varredura nos dados da `stdin` (entrada padrão):

`{{command}} | clamscan -`

- Especifica um arquivo de banco de dados de vírus ou diretório de arquivos:

`clamscan --database {{caminho/para/diretório_ou_arquivo_banco_de_dados}}`

- Faz uma varredura no diretório atual e lista apenas os arquivos infectados:

`clamscan --infected`

- Gera um relatório da varredura para um arquivo de registro:

`clamscan --log {{caminho/para/arquivo_de_registro}}`

- Move arquivos infectados para um diretório específico:

`clamscan --move {{caminho/para/diretório_de_quarentena}}`

- Remove arquivos infectados:

`clamscan --remove yes`
