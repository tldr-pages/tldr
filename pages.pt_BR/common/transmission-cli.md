# transmission-cli

> Um cliente BitTorrent leve e de linha de comando.
> Esta ferramenta foi descontinuada. Por favor, veja `transmission-remote`.
> Mais informações: <https://transmissionbt.com>.

- Baixa um torrent específico:

`transmission-cli {{url|magnet|caminho/para/arquivo}}`

- Baixa um torrent para um diretório específico:

`transmission-cli --download-dir {{caminho/para/diretório_download}} {{url|magnet|caminho/para/arquivo}}`

- Cria um arquivo torrent de um arquivo ou diretório específico:

`transmission-cli --new {{caminho/para/arquivo_ou_diretório_origem}}`

- Especifica o limite de velocidade de download (em KB/s):

`transmission-cli --downlimit {{50}} {{url|magnet|caminho/para/arquivo}}`

- Especifica o limite de velocidade de upload (em KB/s):

`transmission-cli --uplimit {{50}} {{url|magnet|caminho/para/arquivo}}`

- Usa uma porta específica para conexões:

`transmission-cli --port {{número_porta}} {{url|magnet|caminho/para/arquivo}}`

- Força criptografia para conexões com pares:

`transmission-cli --encryption-required {{url|magnet|caminho/para/arquivo}}`

- Usa uma lista de bloqueio de pares formatados em Bluetack:

`transmission-cli --blocklist {{url_lista_bloqueio|caminho/para/lista_bloqueio}} {{url|magnet|caminho/para/arquivo}}`
