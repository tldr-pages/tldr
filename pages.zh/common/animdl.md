# animdl

> 搜索、流媒体播放和下载动漫。
> 另请参阅：`ani-cli`。
> 更多信息：<https://github.com/justfoolingaround/animdl#usage>。

- 下载特定动漫：

`animdl download "{{动漫标题}}"`

- 通过指定剧集范围下载特定动漫：

`animdl download "{{动漫标题}}" {{[-r|--range]}} {{起始剧集}}-{{结束剧集}}`

- 通过指定下载目录下载特定动漫：

`animdl download "{{动漫标题}}" {{[-d|--download-dir]}} {{路径/到/目录}}`

- 获取特定动漫的流媒体 URL：

`animdl grab "{{动漫标题}}"`

- 显示下周即将播出的动漫时间表：

`animdl schedule`

- 搜索特定动漫：

`animdl search "{{动漫标题}}"`

- 流媒体播放特定动漫：

`animdl stream "{{动漫标题}}"`

- 流媒体播放特定动漫的最新一集：

`animdl stream "{{动漫标题}}" {{[-s|--special]}} latest`
