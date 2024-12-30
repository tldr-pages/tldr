# peerflix

> 将基于视频或音频的种子流式传输到媒体播放器。
> 更多信息：<https://github.com/mafintosh/peerflix>。

- 流式传输种子中最大的媒体文件：

`peerflix "{{torrent_url|magnet_link}}"`

- 列出种子中所有可流式传输的文件（以磁力链接给出）：

`peerflix "{{magnet:?xt=urn:btih:0123456789abcdef0123456789abcdef01234567}}" --list`

- 将种子中最大的文件（以种子URL给出）流式传输到 VLC：

`peerflix "{{http://example.net/music.torrent}}" --vlc`

- 将种子中最大的文件流式传输到 MPlayer，并带有字幕：

`peerflix "{{torrent_url|magnet_link}}" --mplayer --subtitles {{subtitle-file.srt}}`

- 将种子中的所有文件流式传输到 Airplay：

`peerflix "{{torrent_url|magnet_link}}" --all --airplay`