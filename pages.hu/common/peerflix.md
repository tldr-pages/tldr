# peerflix

> Videó- vagy hangalapú torrentek streamelése médialejátszóra. További információ: <https://github.com/mafintosh/peerflix>.

- A torrent legnagyobb médiafájljának streamelése:

`peerflix "{{torrent_url|magnet_link}}"`

- A torrentben található összes streamelhető fájl listázása (mágneses linkként megadva):

`peerflix "{{magnet:?xt=urn:btih:0123456789abcdef0123456789abcdef01234567}}" --list`

- A torrentben lévő legnagyobb fájl streamelése a VLC-be, torrent URL-címként megadva:

`peerflix "{{http://example.net/music.torrent}}" --vlc`

- A torrent legnagyobb fájljának streamelése MPlayerre, feliratokkal:

`peerflix "{{torrent_url|magnet_link}}" --mplayer --subtitles {{subtitle-file.srt}}`

- A torrent összes fájljának streamelése Airplay-re:

`peerflix "{{torrent_url|magnet_link}}" --all --airplay`
