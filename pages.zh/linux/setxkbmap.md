# setxkbmap

> 使用 X 键盘扩展设置键盘。
> 更多信息：<https://manned.org/setxkbmap>。

- 将键盘设置为法语 AZERTY：

`setxkbmap {{fr}}`

- 设置多个键盘布局、它们的变体和切换选项：

`setxkbmap -layout {{us,de}} -variant {{,qwerty}} -option {{'grp:alt_caps_toggle'}}`

- 获取帮助：

`setxkbmap -help`

- 列出所有布局：

`localectl list-x11-keymap-layouts`

- 列出布局的变体：

`localectl list-x11-keymap-variants {{de}}`

- 列出可用的切换选项：

`localectl list-x11-keymap-options | grep grp:`