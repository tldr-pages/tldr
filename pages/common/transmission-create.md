# transmission-create

> Create BitTorrent `.torrent` files.
> See also: `transmission`.
> More information: <https://manned.org/transmission-create>.

- Create a torrent with 2048 KB as the piece size:

`transmission-create {{[-o|--outfile]}} {{path/to/example.torrent}} {{[-t|--tracker]}} {{tracker_announce_url}} {{[-s|--piecesize]}} {{2048}} {{path/to/file_or_directory}}`

- Create a private torrent with a 2048 KB piece size:

`transmission-create {{[-p|--private]}} {{[-o|--outfile]}} {{path/to/example.torrent}} {{[-t|--tracker]}} {{tracker_announce_url}} {{[-s|--piecesize]}} {{2048}} {{path/to/file_or_directory}}`

- Create a torrent with a comment:

`transmission-create {{[-o|--outfile]}} {{path/to/example.torrent}} {{[-t|--tracker]}} {{tracker_url1}} {{[-c|--comment]}} {{comment}} {{path/to/file_or_directory}}`

- Create a torrent with multiple trackers:

`transmission-create {{[-o|--outfile]}} {{path/to/example.torrent}} {{[-t|--tracker]}} {{tracker_url1}} {{[-t|--tracker]}} {{tracker_url2}} {{path/to/file_or_directory}}`

- Display help page:

`transmission-create {{[-h|--help]}}`
