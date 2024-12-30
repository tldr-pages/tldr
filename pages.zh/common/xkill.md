# xkill

> 在图形会话中以交互方式终止一个窗口。
> 另见：`kill`，`killall`。
> 更多信息：<https://www.x.org/releases/current/doc/man/man1/xkill.1.xhtml>。

- 显示一个光标，按下左键终止一个窗口（按下其他任意鼠标按钮以取消）：

`xkill`

- 显示一个光标，通过按下任意鼠标按钮选择要终止的窗口：

`xkill -button any`

- 使用特定的ID终止一个窗口（使用`xwininfo`获取窗口信息）：

`xkill -id {{id}}`