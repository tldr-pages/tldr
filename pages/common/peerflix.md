# peerflix

> Stream video- or audio-based torrents to a media player.
> More information: <https://github.com/mafintosh/peerflix>.

- Stream the largest media file in a torrent:

`peerflix "{{torrent_url|magnet_link}}"`

- List all streamable files contained in a torrent (given as a magnet link):

`peerflix "{{magnet:?xt=urn:btih:0123456789abcdef0123456789abcdef01234567}}" --list`

- Stream the largest file in a torrent, given as a torrent URL, to VLC:

`peerflix "{{http://example.net/music.torrent}}" --vlc`

- Stream the largest file in a torrent to MPlayer, with subtitles:

`peerflix "{{torrent_url|magnet_link}}" --mplayer --subtitles {{subtitle-file.srt}}`

- Stream all files from a torrent to Airplay:

`peerflix "{{torrent_url|magnet_link}}" --all --airplay`
