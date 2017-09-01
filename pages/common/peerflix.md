# peerflix

> Stream video- or audio-based torrents to a media player.

- Stream the largest media file in a torrent given as a magnet link:

`peerflix "{{magnet:?xt=urn:btih:0123456789abcdef0123456789abcdef01234567}}"`

- Stream the largest file in a torrent, given as a torrent URL, to VLC:

`peerflix "{{http://example.net/music.torrent}}" --vlc`

- Stream the largest file in a torrent to MPlayer, with subtitles:

`peerflix "{{torrent_url|magnet_link}}" --mplayer --subtitles subtitle-file.srt`

- Stream all files from a torrent to Airplay:

`peerflix "{{torrent_url|magnet_link}}" --all --airplay`

- List the files in a torrent that are available for streaming:

`peerflix "{{torrent_url|magnet_link}}" --list`
