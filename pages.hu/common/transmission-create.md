# transmission-create

> CLI segédprogram BitTorrent .torrent fájlok létrehozására. További információ: <https://manned.org/transmission-create>.

- Létrehoz egy torrentet 2048 KB-os darabmérettel:

`transmission-create -o {{path/to/example.torrent}} --tracker {{tracker_announce_url}} --piecesize {{2048}} {{path/to/file_or_directory}}`

- Privát torrent létrehozása 2048 KB-os darabmérettel:

`transmission-create -p -o {{path/to/example.torrent}} --tracker {{tracker_announce_url}} --piecesize {{2048}} {{path/to/file_or_directory}}`

- Hozzászólással ellátott torrent létrehozása:

`transmission-create -o {{path/to/example.torrent}} --tracker {{tracker_url1}} -c {{comment}} {{path/to/file_or_directory}}`

- Torrent létrehozása több nyomkövetővel:

`transmission-create -o {{path/to/example.torrent}} --tracker {{tracker_url1}} --tracker {{tracker_url2}} {{path/to/file_or_directory}}`

- Súgóoldal megjelenítése:

`transmission-create --help`
