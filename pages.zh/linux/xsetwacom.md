# xsetwacom

> 命令行工具，用于在运行时更改 Wacom 画笔平板的设置。
> 更多信息：<https://manned.org/xsetwacom>。

- 列出所有可用的 Wacom 设备。设备名称在第一列：

`xsetwacom list`

- 将 Wacom 区域设置为特定屏幕。使用 `xrandr` 获取屏幕名称：

`xsetwacom set "{{device_name}}" MapToOutput {{screen}}`

- 将模式设置为相对（像鼠标一样）或绝对（像笔一样）模式：

`xsetwacom set "{{device_name}}" Mode "{{Relative|Absolute}}"`

- 将输入旋转（对于平板电脑在旋转屏幕时非常有用），从“自然”旋转旋转 0|90|180|270 度：

`xsetwacom set "{{device_name}}" Rotate {{none|half|cw|ccw}}`

- 设置按钮仅在笔尖接触平板时工作：

`xsetwacom set "{{device_name}}" TabletPCButton "on"`