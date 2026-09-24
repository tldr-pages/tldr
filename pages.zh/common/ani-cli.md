# ani-cli

> 一个用于浏览和观看动漫的命令行工具。
> 另请参阅：`animdl`。
> 更多信息：<https://manned.org/ani-cli>。

- 按名称搜索动漫：

`ani-cli "{{动漫名称}}"`

- 下载（[d]ownload）剧集：

`ani-cli {{[-d|--download]}} "{{动漫名称}}"`

- 下载（[d]ownload）一个范围（[r]ange）的剧集：

`ani-cli {{[-d|--download]}} {{[-r|--range]}} "{{1 6}}" "{{动漫名称}}"`

- 下载（[d]ownload）整部动漫（所有剧集的范围）：

`ani-cli {{[-d|--download]}} {{[-r|--range]}} "1 -1" "{{动漫名称}}"`

- 使用 [v]LC 播放器播放：

`ani-cli {{[-v|--vlc]}} "{{动漫名称}}"`

- 观看特定（[e]pisode）剧集：

`ani-cli {{[-e|--episode]}} {{剧集序号}} "{{动漫名称}}"`

- 从历史记录中（[c]ontinue）继续观看动漫：

`ani-cli {{[-c|--continue]}}`

- 更新（[U]pdate）`ani-cli`：

`ani-cli {{[-U|--update]}}`
