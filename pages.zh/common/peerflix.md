# peerflix

> 将基于视频或音频的torrent流式传输到媒体播放器。
> 更多信息：<https://github.com/mafintosh/peerflix>。

- 流式传输torrent中的最大媒体文件：

`peerflix "{{torrent_url|magnet_link}}"`

- 列出torrent（作为磁力链接提供）中所有可流式传输的文件：

`peerflix "{{magnet:?xt=urn:btih:0123456789abcdef0123456789abcdef01234567}}" --list`

- 流式传输作为torrent URL提供的torrent中的最大文件到VLC：

`peerflix "{{http://example.net/music.torrent}}" --vlc`

- 流式传输torrent中的最大文件到MPlayer，并使用字幕：

`peerflix "{{torrent_url|magnet_link}}" --mplayer --subtitles {{subtitle-file.srt}}`

- 流式传输torrent中的所有文件到Airplay：

`peerflix "{{torrent_url|magnet_link}}" --all --airplay`