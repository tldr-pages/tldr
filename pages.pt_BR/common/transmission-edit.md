# transmission-edit

> Modifica URLs de anúncio a partir de arquivos de torrent.
> Veja também: `transmission`.
> Mais informações: <https://manned.org/transmission-edit>.

- Adiciona ou remove uma URL a partir da lista de anúncio do torrent:

`transmission-edit --{{add|delete}} {{http://example.com}} {{caminho/para/arquivo.torrent}}`

- Atualiza um código do rastreador em um arquivo de torrent:

`transmission-edit --replace {{antigo-código}} {{novo-código}} {{caminho/para/arquivo.torrent}}`
