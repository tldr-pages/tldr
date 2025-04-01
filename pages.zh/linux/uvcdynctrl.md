# uvcdynctrl

> 一个用于管理 uvcvideo 中动态控制的 libwebcam 命令行工具。
> 更多信息：<https://manned.org/uvcdynctrl>.

- 列出所有可用的摄像头：

`uvcdynctrl -l`

- 使用特定的设备（默认为 `video0`）：

`uvcdynctrl -d {{device_name}}`

- 列出所有可用的控制项：

`uvcdynctrl -c`

- 设置新的控制值（对于负值，使用 `-- -value`）：

`uvcdynctrl -s {{control_name}} {{value}}`

- 获取当前的控制值：

`uvcdynctrl -g {{control_name}}`

- 将当前控制项的状态保存到文件中：

`uvcdynctrl -W {{filename}}`

- 从文件中加载控制项的状态：

`uvcdynctrl -L {{filename}}`