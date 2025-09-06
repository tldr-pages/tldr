# clamdscan

> Faz uma varredura em busca de vírus usando o ClamAV Daemon.
> Mais informações: <https://docs.clamav.net/manual/Usage/Scanning.html#clamdscan>.

- Faz uma varredura em um arquivo ou diretório por vulnerabilidades:

`clamdscan {{caminho/para/arquivo_ou_diretório}}`

- Faz uma varredura nos dados da `stdin` (entrada padrão):

`{{comando}} | clamdscan -`

- Faz uma varredura no diretório atual e lista apenas os arquivos infectados:

`clamdscan --infected`

- Gera um relatório da varredura para um arquivo de registro:

`clamdscan --log {{caminho/para/arquivo_de_registro}}`

- Move arquivos infectados para um diretório específico:

`clamdscan --move {{caminho/para/diretório_de_quarentena}}`

- Remove arquivos infectados:

`clamdscan --remove`

- Usa várias threads para para fazer uma varredura em um diretório:

`clamdscan --multiscan`

- Passa o descritor de arquivo em vez de transmitir o arquivo para o daemon:

`clamdscan --fdpass`
