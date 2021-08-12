# transmission-create

> Un utilitar CLI pentru a crea fișiere BitTorrent .torrent.
> Mai multe informaţii: <https://manned.org/transmission-create>

- Creați un torent cu 2048 KB ca dimensiune piesă:

`transmission-create -o {{path/to/example.torrent}} --tracker {{tracker_announce_url}} --piecesize {{2048}} {{path/to/file_or_directory}}`

- Creați un torrent privat cu o dimensiune de 2048 KB:

`transmission-create -p -o {{path/to/example.torrent}} --tracker {{tracker_announce_url}} --piecesize {{2048}} {{path/to/file_or_directory}}`

- Creați un torent cu un comentariu:

`transmission-create -o {{path/to/example.torrent}} --tracker {{tracker_url1}} -c {{comment}} {{path/to/file_or_directory}}`

- Creați un torent cu mai multe trackere:

`transmission-create -o {{path/to/example.torrent}} --tracker {{tracker_url1}} --tracker {{tracker_url2}} {{path/to/file_or_directory}}`

- Arată pagina de ajutor:

`transmission-create --help`
