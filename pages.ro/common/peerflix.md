# peerflix

> Redați în flux torrente video sau audio pe un player media.
> Mai multe informaţii: <https://github.com/mafintosh/peerflix>

- Stream cel mai mare fișier media într-un torent:

`peerflix "{{torrent_url|magnet_link}}"`

- Listează toate fișierele streamable conținute într-un torent (dat ca un link magnet):

`peerflix "{{magnet:?xt=urn:btih:0123456789abcdef0123456789abcdef01234567}}" --list`

- Stream cel mai mare fișier într-un torent, dat ca un URL torrent, la VLC:

`peerflix "{{http://example.net/music.torrent}}" --vlc`

- Stream cel mai mare fișier într-un torrent la MPlayer, cu subtitrări:

`peerflix "{{torrent_url|magnet_link}}" --mplayer --subtitles {{subtitle-file.srt}}`

- Transmite toate fișierele de la un torent la Airplay:

`peerflix "{{torrent_url|magnet_link}}" --all --airplay`
