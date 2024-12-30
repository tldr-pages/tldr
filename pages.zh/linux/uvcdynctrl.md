# uvcdynctrl

> 一款用于管理uvcvideo中动态控制的libwebcam命令行工具。
> 更多信息：<https://manned.org/uvcdynctrl>。

- 列出所有可用的摄像头：

`uvcdynctrl -l`

- 使用特定设备（默认为`video0`）：

`uvcdynctrl -d {{device_name}}`

- 列出可用的控制项：

`uvcdynctrl -c`

- 设置新的控制值（对于负值，请使用`-- -value`）：

`uvcdynctrl -s {{control_name}} {{value}}`

- 获取当前控制值：

`uvcdynctrl -g {{control_name}}`

- 将当前控制状态保存到文件：

`uvcdynctrl -W {{filename}}`

- 从文件加载控制状态：

`uvcdynctrl -L {{filename}}`