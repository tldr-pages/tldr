# playerctl

> 通过 MPRIS 控制媒体播放器。
> 更多信息：<https://github.com/altdesktop/playerctl>.

- 切换播放状态：

`playerctl play-pause`

- 跳到下一首曲目：

`playerctl next`

- 返回上一首曲目：

`playerctl previous`

- 列出所有播放器：

`playerctl --list-all`

- 向特定播放器发送命令：

`playerctl --player {{player_name}} {{play-pause|next|previous|...}}`

- 向所有播放器发送命令：

`playerctl --all-players {{play-pause|next|previous|...}}`

- 显示当前曲目的元数据：

`playerctl metadata --format "{{现在播放: \{\{artist\}\} - \{\{album\}\} - \{\{title\}\}}}"`
