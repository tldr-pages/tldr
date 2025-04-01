# xsetwacom

> 用于在运行时更改 Wacom 笔平板设备设置的命令行工具。
> 更多信息：<https://manned.org/xsetwacom>。

- 列出所有可用的 Wacom 设备。设备名称在第一列：

`xsetwacom list`

- 将 Wacom 区域设置为特定屏幕。使用 `xrandr` 获取屏幕名称：

`xsetwacom set "{{device_name}}" MapToOutput {{screen}}`

- 设置模式为相对（如鼠标）或绝对（如笔）模式：

`xsetwacom set "{{device_name}}" Mode "{{Relative|Absolute}}"`

- 旋转输入（对平板电脑旋转屏幕时特别有用），从“自然”旋转的角度旋转 0|90|180|270 度：

`xsetwacom set "{{device_name}}" Rotate {{none|half|cw|ccw}}`

- 设置按钮仅在笔尖触碰平板时生效：

`xsetwacom set "{{device_name}}" TabletPCButton "on"`