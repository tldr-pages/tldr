# deemix

> 一个从 Deezloader Remix 的废墟中构建的简易 Deezer 下载库。
> 它可以作为独立的 CLI 应用程序使用，或通过 API 实现到 UI 中。
> 更多信息：<https://gitlab.com/RemixDev/deemix-py>。

- 下载一首曲目或播放列表：

`deemix {{https://www.deezer.com/us/track/00000000}}`

- 以特定比特率下载曲目/播放列表：

`deemix --bitrate {{FLAC|MP3}} {{url}}`

- 下载到特定路径：

`deemix --bitrate {{bitrate}} --path {{path}} {{url}}`

- 在当前目录创建一个可携带的 deemix 配置文件：

`deemix --portable --bitrate {{bitrate}} --path {{path}} {{url}}`