# spotdl

> 下载 Spotify 播放列表和歌曲及其元数据。
> 更多信息：<https://github.com/spotDL/spotify-downloader>。

- 从提供的 URL 下载歌曲并嵌入元数据：

`spotdl {{open.spotify.com/playlist/playlistId open.spotify.com/track/trackId ...}}`

- 启动一个 Web 界面以下载单个歌曲：

`spotdl web`

- 仅保存元数据而不下载任何内容：

`spotdl save {{open.spotify.com/playlist/playlistId ...}} --save-file {{path/to/save_file.spotdl}}`