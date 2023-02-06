# deluge

> Parancssori BitTorrent kliens. További információ: <https://deluge-torrent.org>.

- Torrent letöltése:

`deluge {{url|magnet|path/to/file}}`

- Egy torrent letöltése egy adott konfigurációs fájl segítségével:

`deluge -c {{path/to/configuration_file}} {{url|magnet|path/to/file}}`

- Egy torrent letöltése és a megadott felhasználói felület elindítása:

`deluge -u {{gtk|web|console}} {{url|magnet|path/to/file}}`

- Torrent letöltése és a napló kimenete egy fájlba:

`deluge -l {{path/to/log_file}} {{url|magnet|path/to/file}}`
