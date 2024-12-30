# xfce4-screenshooter

> XFCE4 截图工具。
> 更多信息：<https://docs.xfce.org/apps/xfce4-screenshooter/start>。

- 启动截图工具 GUI：

`xfce4-screenshooter`

- 截取整个屏幕的截图，并启动 GUI 询问如何继续：

`xfce4-screenshooter --fullscreen`

- 截取整个屏幕的截图，并将其保存在指定目录中：

`xfce4-screenshooter --fullscreen --save {{path/to/directory}}`

- 在截屏前等待一段时间：

`xfce4-screenshooter --delay {{seconds}}`

- 截取屏幕的某个区域（使用鼠标选择）：

`xfce4-screenshooter --region`

- 截取活动窗口的截图，并将其复制到剪贴板：

`xfce4-screenshooter --window --clipboard`

- 截取活动窗口的截图，并使用选定的程序打开：

`xfce4-screenshooter --window --open {{gimp}}`