# you-get

> 从网络下载媒体内容（视频、音频、图片）。
> 另见：`yt-dlp`，`youtube-viewer`，`instaloader`。
> 更多信息：<https://you-get.org>。

- 打印关于网络上特定媒体的信息：

`you-get --info {{https://example.com/video?id=value}}`

- 从特定 URL 下载媒体：

`you-get {{https://example.com/video?id=value}}`

- 在 Google 视频上搜索并下载：

`you-get {{关键词}}`

- 下载媒体到特定位置：

`you-get --output-dir {{路径/到/目录}} --output-filename {{文件名}} {{https://example.com/watch?v=value}}`

- 使用代理下载媒体：

`you-get --http-proxy {{代理服务器}} {{https://example.com/watch?v=value}}`