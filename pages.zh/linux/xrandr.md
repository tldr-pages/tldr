# xrandr

> 设置屏幕输出的尺寸、方向和/或镜像。
> 更多信息：<https://www.x.org/releases/current/doc/man/man1/xrandr.1.xhtml>.

- 显示系统当前状态（已知屏幕、分辨率等）：

`xrandr {{[-q|--query]}}`

- 关闭未连接的输出设备，启用已连接的输出设备并使用默认设置：

`xrandr --auto`

- 将 DisplayPort 1 的分辨率和更新频率更改为 1920x1080，60Hz：

`xrandr --output {{DP1}} --mode {{1920x1080}} --rate {{60}}`

- 将 HDMI2 的分辨率设置为 1280x1024，并将其放在 DP1 的右侧：

`xrandr --output {{HDMI2}} --mode {{1280x1024}} --right-of {{DP1}}`

- 关闭 VGA1 输出：

`xrandr --output {{VGA1}} --off`

- 将 LVDS1 的亮度设置为 50%：

`xrandr --output {{LVDS1}} --brightness {{0.5}}`

- 显示任何 X 服务器的当前状态：

`xrandr {{[-d|--display]}} :{{0}} {{[-q|--query]}}`
