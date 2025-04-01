# deemix

> 一个从 Deezloader Remix 的废墟中重建的 Deezer 下载器库。
> 可以作为独立的 CLI 应用程序使用，也可以通过 API 在用户界面中实现。
> 更多信息：<https://gitlab.com/RemixDev/deemix-py>.

- 下载单曲或播放列表：

`deemix {{https://www.deezer.com/us/track/00000000}}`

- 以特定比特率下载单曲/播放列表：

`deemix --bitrate {{FLAC|MP3}} {{url}}`

- 下载到指定路径：

`deemix --bitrate {{bitrate}} --path {{path}} {{url}}`

- 在当前目录中创建一个便携式 deemix 配置文件：

`deemix --portable --bitrate {{bitrate}} --path {{path}} {{url}}`
