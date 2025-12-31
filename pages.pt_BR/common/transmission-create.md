# transmission-create

> Cria arquivos BitTorrent `.torrent`.
> Veja também: `transmission`.
> Mais informações: <https://manned.org/transmission-create>.

- Cria um torrent com 2048 KB como o tamanho da parte:

`transmission-create {{[-o|--outfile]}} {{caminho/para/exemplo.torrent}} {{[-t|--tracker]}} {{url_anuncio_tracker}} {{[-s|--piecesize]}} {{2048}} {{caminho/para/arquivo_ou_diretório}}`

- Cria um torrent privado com um tamanho de parte de 2048 KB:

`transmission-create {{[-p|--private]}} {{[-o|--outfile]}} {{caminho/para/exemplo.torrent}} {{[-t|--tracker]}} {{url_anuncio_tracker}} {{[-s|--piecesize]}} {{2048}} {{caminho/para/arquivo_ou_diretório}}`

- Cria um torrent com um comentário:

`transmission-create {{[-o|--outfile]}} {{caminho/para/exemplo.torrent}} {{[-t|--tracker]}} {{url_rastreador1}} {{[-c|--comment]}} {{comentário}} {{caminho/para/arquivo_ou_diretório}}`

- Cria um torrent com vários rastreadores:

`transmission-create {{[-o|--outfile]}} {{caminho/para/exemplo.torrent}} {{[-t|--tracker]}} {{url_rastreador1}} {{[-t|--tracker]}} {{url_rastreador2}} {{caminho/para/arquivo_ou_diretório}}`

- Exibe a página de ajuda:

`transmission-create {{[-h|--help]}}`
