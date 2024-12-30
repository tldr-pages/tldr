# caffeinate

> 防止 macOS 进入睡眠状态。
> 更多信息：<https://keith.github.io/xcode-man-pages/caffeinate.8.html>。

- 防止睡眠 1 小时（3600 秒）：

`caffeinate -u -t {{3600}}`

- 防止睡眠直到命令完成：

`caffeinate -s "{{command}}"`

- 防止睡眠直到指定 PID 的进程完成：

`caffeinate -w {{pid}}`

- 防止睡眠（使用 `Ctrl + C` 退出）：

`caffeinate -i`

- 防止磁盘进入睡眠状态（使用 `Ctrl + C` 退出）：

`caffeinate -m`