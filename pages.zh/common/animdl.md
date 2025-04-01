# animdl

> 高效、强大且快速的动漫爬虫工具。
> 参见: `ani-cli`。
> 更多信息: <https://github.com/justfoolingaround/animdl>。

- 下载特定的动漫：

`animdl download {{anime_title}}`

- 通过指定剧集范围下载特定的动漫：

`animdl download {{anime_title}} {{[-r|--range]}} {{start_episode}}-{{end_episode}}`

- 通过指定下载目录下载特定的动漫：

`animdl download {{anime_title}} {{[-d|--download-dir]}} {{path/to/download_directory}}`

- 获取特定动漫的流媒体URL：

`animdl grab {{anime_title}}`

- 显示下周的动漫播放时间表：

`animdl schedule`

- 搜索特定的动漫：

`animdl search {{anime_title}}`

- 播放特定的动漫：

`animdl stream {{anime_title}}`

- 播放特定动漫的最新剧集：

`animdl stream {{anime_title}} {{[-s|--special]}} latest`