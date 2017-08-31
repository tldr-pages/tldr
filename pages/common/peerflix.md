# peerflix

> Stream video or audio based torrents to your favorite player.

- Stream a torrent:

`peerflix "{{magnet:?xt=urn:btih:00112233445566}}"`

- Stream a torrent to VLC:

`peerflix "{{torrent url|magnet link}}" --vlc`

- Stream all files from a torrent to Airplay:

`peerflix "{{torrent url|magnet link}}" --all --airplay`
