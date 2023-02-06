# transmission-cli

> Könnyű, parancssori BitTorrent kliens. Ez az eszköz elavult, lásd: `transmission-remote`. További információ: <https://transmissionbt.com>.

- Egy adott torrent letöltése:

`transmission-cli {{url|magnet|path/to/file}}`

- Egy torrent letöltése egy adott könyvtárba:

`transmission-cli --download-dir {{path/to/download_directory}} {{url|magnet|path/to/file}}`

- Torrent fájl létrehozása egy adott fájlból vagy könyvtárból:

`transmission-cli --new {{path/to/source_file_or_directory}}`

- A letöltési sebességhatár beállítása 50 KB/s-ra:

`transmission-cli --downlimit {{50}} {{url|magnet|path/to/file}}`

- A feltöltési sebességhatár beállítása 50 KB/s-ra:

`transmission-cli --uplimit {{50}} {{url|magnet|path/to/file}}`

- Egy adott port használata a kapcsolatokhoz:

`transmission-cli --port {{port_number}} {{url|magnet|path/to/file}}`

- Titkosítás kikényszerítése a társkapcsolatokhoz:

`transmission-cli --encryption-required {{url|magnet|path/to/file}}`

- Bluetack-formátumú társkapcsolati blokklista használata:

`transmission-cli --blocklist {{blocklist_url|path/to/blocklist}} {{url|magnet|path/to/file}}`
