# bspc

> 配置和控制 `bspwm`，管理节点、桌面、显示器等。
> 另见： `bspwm`。
> 更多信息： <https://github.com/baskerville/bspwm>。

- 定义两个虚拟桌面：

`bspc monitor --reset-desktops {{desktop_name1}} {{desktop_name2}}`

- 聚焦给定的桌面：

`bspc desktop --focus {{number}}`

- 关闭选定节点根部的窗口：

`bspc node --close`

- 将选定节点发送到给定桌面：

`bspc node --to-desktop {{number}}`

- 切换选定节点的全屏模式：

`bspc node --state ~fullscreen`

- 设置特定设置的值：

`bspc config {{setting_name}} {{value}}`