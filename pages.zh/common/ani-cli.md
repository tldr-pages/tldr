# ani-cli

> 一个用于浏览和观看动漫的命令行工具。
> 更多信息：<https://manned.org/ani-cli>.

- 按名称搜索动漫：

`ani-cli "{{动漫名称}}"`

- 下载（[d]ownload）剧集：

`ani-cli -d "{{动漫名称}}"`

- 下载（[d]ownload）一个范围（[r]ange）的剧集：

`ani-cli -d -r "{{1 6}}" "{{动漫名称}}"`

- 下载（[d]ownload）整部动漫（所有剧集的范围）：

`ani-cli -d -r "1 -1" "{{动漫名称}}"`

- 使用 [v]LC 播放器播放：

`ani-cli -v "{{动漫名称}}"`

- 观看特定（[e]pisode）剧集：

`ani-cli -e {{剧集序号}} "{{动漫名称}}"`

- 从历史记录中（[c]ontinue）继续观看动漫：

`ani-cli -c`

- 更新（[U]pdate）`ani-cli`：

`ani-cli -U`
