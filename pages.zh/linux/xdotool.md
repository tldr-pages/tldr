# xdotool

> 用于 X11 的命令行自动化工具。
> 更多信息：<https://manned.org/xdotool>。

- 获取正在运行的 Firefox 窗口的 X-Windows 窗口 ID：

`xdotool search --onlyvisible --name {{firefox}}`

- 执行鼠标 `<右键点击>`：

`xdotool click {{3}}`

- 获取当前活动窗口的 ID：

`xdotool getactivewindow`

- 将焦点设置到窗口 ID 为 12345 的窗口上：

`xdotool windowfocus --sync {{12345}}`

- 输入消息，每个字母之间有 500 毫秒的延迟：

`xdotool type --delay {{500}} "Hello world"`

- 按下 `<回车>` 键：

`xdotool key {{KP_Enter}}`
