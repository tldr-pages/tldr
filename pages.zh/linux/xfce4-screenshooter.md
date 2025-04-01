# xfce4-screenshooter

> XFCE4 截图工具。
> 更多信息：<https://docs.xfce.org/apps/xfce4-screenshooter/start>。

- 启动截图工具的 GUI 界面：

`xfce4-screenshooter`

- 对整个屏幕进行截图，并启动 GUI 询问如何处理：

`xfce4-screenshooter --fullscreen`

- 对整个屏幕进行截图，并保存到指定目录：

`xfce4-screenshooter --fullscreen --save {{path/to/directory}}`

- 在截图前等待一段时间：

`xfce4-screenshooter --delay {{seconds}}`

- 对屏幕的某个区域进行截图（使用鼠标选择区域）：

`xfce4-screenshooter --region`

- 对活动窗口进行截图，并复制到剪贴板：

`xfce4-screenshooter --window --clipboard`

- 对活动窗口进行截图，并使用选定的程序打开：

`xfce4-screenshooter --window --open {{gimp}}`
