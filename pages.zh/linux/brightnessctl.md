# brightnessctl

> GUN/Linux 操作系统上用来读取和控制设备亮度的实用工具。
> 更多信息：<https://github.com/Hummer12007/brightnessctl>.

- 列出亮度可变的设备：

`brightnessctl --list`

- 打印显示器当前亮度：

`brightnessctl get`

- 将显示器背光的亮度设置为指定的百分比：

`brightnessctl set {{50%}}`

- 按指定的增量增加亮度：

`brightnessctl set {{+10%}}`

- 将亮度降低指定的递减量：

`brightnessctl set {{10%-}}`
