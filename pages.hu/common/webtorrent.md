# webtorrent

> A WebTorrent parancssori interfésze. Támogatja a mágneseket, URL-eket, info hash-eket és a `.torrent` fájlokat. További információk: <https://github.com/webtorrent/webtorrent-cli>.

- Torrent letöltése:

`webtorrent download "{{torrent_id}}"`

- Egy torrent streamelése a VLC médialejátszóba:

`webtorrent download "{{torrent_id}}" --vlc`

- Egy torrent streamelése a Digital Living Network Alliance (DLNA) eszközre:

`webtorrent download "{{torrent_id}}" --dlna`

- Egy adott torrenthez tartozó fájlok listájának megjelenítése:

`webtorrent download "{{torrent_id}}" --select`

- A letöltendő torrent fájlindexének megadása:

`webtorrent download "{{torrent_id}}" --select {{index}}`

- Egy adott fájl vagy könyvtár elküldése:

`webtorrent seed {{path/to/file_or_directory}}`

- Új torrentfájl létrehozása a megadott fájlútvonalhoz:

`webtorrent create {{path/to/file}}`

- Egy mágnes URI vagy a `.torrent` fájl információinak megjelenítése:

`webtorrent info {{path/to/file_or_magnet}}`
