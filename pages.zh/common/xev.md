# xev

> 打印X事件的内容。
> 更多信息：<https://gitlab.freedesktop.org/xorg/app/xev>。

- 监控所有发生的X事件：

`xev`

- 监控根窗口的所有X事件，而不是创建一个新窗口：

`xev -root`

- 监控特定窗口的所有X事件：

`xev -id {{window_id}}`

- 监控来自给定类别的X事件（可以多次指定）：

`xev -event {{event_category}}`