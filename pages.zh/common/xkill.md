# xkill

> 在图形会话中以交互方式终止窗口。
> 另请参阅：`kill`、`killall`。
> 更多信息：<https://www.x.org/releases/current/doc/man/man1/xkill.1.xhtml>.

- 按下鼠标左键时终止鼠标选择的窗口（按下任何其他鼠标按钮可取消）：

`xkill`

- 按下任意鼠标按键时终止鼠标选择的窗口：

`xkill -button any`

- 终止具有特定 ID 的窗口（使用 `xwininfo` 获取有关窗口的信息）：

`xkill -id {{id}}`
