# xdotool

> 用于 X11 的命令行自动化。
> 更多信息请访问：<https://manned.org/xdotool>。

- 检索正在运行的 Firefox 窗口的 X-Windows 窗口 ID：

`xdotool search --onlyvisible --name {{firefox}}`

- 点击右键：

`xdotool click {{3}}`

- 获取当前活动窗口的 ID：

`xdotool getactivewindow`

- 聚焦于 ID 为 12345 的窗口：

`xdotool windowfocus --sync {{12345}}`

- 输入一条消息，每个字母延迟 500 毫秒：

`xdotool type --delay {{500}} "Hello world"`

- 按下回车键：

`xdotool key {{KP_Enter}}`