# xrandr

> 设置屏幕输出的大小、方向和/或反射。
> 更多信息：<https://www.x.org/releases/current/doc/man/man1/xrandr.1.xhtml>。

- 显示系统的当前状态（已知的屏幕、分辨率等）：

`xrandr --query`

- 禁用未连接的输出并启用已连接的输出，使用默认设置：

`xrandr --auto`

- 将 DisplayPort 1 的分辨率和刷新率更改为 1920x1080，60Hz：

`xrandr --output {{DP1}} --mode {{1920x1080}} --rate {{60}}`

- 将 HDMI2 的分辨率设置为 1280x1024，并将其放置在 DP1 的右侧：

`xrandr --output {{HDMI2}} --mode {{1280x1024}} --right-of {{DP1}}`

- 禁用 VGA1 输出：

`xrandr --output {{VGA1}} --off`

- 将 LVDS1 的亮度设置为 50%：

`xrandr --output {{LVDS1}} --brightness {{0.5}}`

- 显示任何 X 服务器的当前状态：

`xrandr --display :{{0}} --query`