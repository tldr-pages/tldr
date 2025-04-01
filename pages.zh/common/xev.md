# xev

> 打印 X 事件的内容。
> 更多信息：<https://gitlab.freedesktop.org/xorg/app/xev>.

- 监听所有发生的 X 事件：

`xev`

- 不创建新窗口，而是监听根窗口的所有 X 事件：

`xev -root`

- 监听特定窗口的所有 X 事件：

`xev -id {{window_id}}`

- 监听来自指定类别的 X 事件（可以多次指定）：

`xev -event {{event_category}}`