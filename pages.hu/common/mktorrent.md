# mktorrent

> CLI segédprogram BitTorrent metainfo fájlok létrehozására. További információ: <https://github.com/Rudde/mktorrent>.

- Létrehoz egy torrentet 2^21 KB-os darabmérettel:

`mktorrent -a {{tracker_announce_url}} -l {{21}} -o {{path/to/example.torrent}} {{path/to/file_or_directory}}`

- Privát torrent létrehozása 2^21 KB darabmérettel:

`mktorrent -p -a {{tracker_announce_url}} -l {{21}} -o {{path/to/example.torrent}} {{path/to/file_or_directory}}`

- Hozzon létre egy torrentet megjegyzéssel:

`mktorrent -c "{{comment}}" -a {{tracker_announce_url}} -l {{21}} -o {{path/to/example.torrent}} {{path/to/file_or_directory}}`

- Torrent létrehozása több nyomkövetővel:

`mktorrent -a {{tracker_announce_url,tracker_announce_url_2}} -l {{21}} -o {{path/to/example.torrent}} {{path/to/file_or_directory}}`

- Torrent létrehozása webes magvető URL-címekkel:

`mktorrent -a {{tracker_announce_url}} -w {{web_seed_url}} -l {{21}} -o {{path/to/example.torrent}} {{path/to/file_or_directory}}`
