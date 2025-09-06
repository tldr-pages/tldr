# transmission-create

> Cria arquivos BitTorrent `.torrent`.
> Veja também: `transmission`.
> Mais informações: <https://manned.org/transmission-create>.

- Cria um torrent com 2048 KB como o tamanho da parte:

`transmission-create -o {{caminho/para/exemplo.torrent}} --tracker {{url_anuncio_tracker}} --piecesize {{2048}} {{caminho/para/arquivo_ou_diretório}}`

- Cria um torrent privado com um tamanho de parte de 2048 KB:

`transmission-create -p -o {{caminho/para/exemplo.torrent}} --tracker {{url_anuncio_tracker}} --piecesize {{2048}} {{caminho/para/arquivo_ou_diretório}}`

- Cria um torrent com um comentário:

`transmission-create -o {{caminho/para/exemplo.torrent}} --tracker {{url_rastreador1}} -c {{comentário}} {{caminho/para/arquivo_ou_diretório}}`

- Cria um torrent com vários rastreadores:

`transmission-create -o {{caminho/para/exemplo.torrent}} --tracker {{url_rastreador1}} --tracker {{url_rastreador2}} {{caminho/para/arquivo_ou_diretório}}`

- Exibe a página de ajuda:

`transmission-create --help`
