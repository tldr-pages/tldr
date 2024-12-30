# brightnessctl

> 用于读取和控制Linux操作系统设备亮度的工具。
> 更多信息请访问：<https://github.com/Hummer12007/brightnessctl>。

- 列出可以调节亮度的设备：

`brightnessctl --list`

- 打印当前显示背光的亮度：

`brightnessctl get`

- 将显示背光的亮度设置为指定的百分比（在范围内）：

`brightnessctl set {{50%}}`

- 按指定增量增加亮度：

`brightnessctl set {{+10%}}`

- 按指定减量减少亮度：

`brightnessctl set {{10%-}}`