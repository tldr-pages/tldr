# mktorrent

> Un utilitar CLI pentru a crea fișiere metainfo BitTorrent.
> Mai multe informaţii: <https://github.com/Rudde/mktorrent>

- Creați un torent cu 2^21 KB ca dimensiune piesă:

`mktorrent -a {{tracker_announce_url}} -l {{21}} -o {{path/to/example.torrent}} {{path/to/file_or_directory}}`

- Creați un torent privat cu o dimensiune de 2^21 KB:

`mktorrent -p -a {{tracker_announce_url}} -l {{21}} -o {{path/to/example.torrent}} {{path/to/file_or_directory}}`

- Creați un torent cu un comentariu:

`mktorrent -c "{{comment}}" -a {{tracker_announce_url}} -l {{21}} -o {{path/to/example.torrent}} {{path/to/file_or_directory}}`

- Creați un torent cu mai multe trackere:

`mktorrent -a {{tracker_announce_url,tracker_announce_url_2}} -l {{21}} -o {{path/to/example.torrent}} {{path/to/file_or_directory}}`

- Creați un torent cu URL-uri de semințe web:

`mktorrent -a {{tracker_announce_url}} -w {{web_seed_url}} -l {{21}} -o {{path/to/example.torrent}} {{path/to/file_or_directory}}`
