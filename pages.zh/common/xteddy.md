# xteddy

> 一个可爱的泰迪熊在你的 X Windows 桌面上。
> 更多信息：<https://manned.org/xteddy.1>。

- 在你的 X 桌面上显示一个可爱的泰迪熊：

`xteddy`

- 使用窗口管理器显示泰迪熊，并忽略 "退出" (`q`) 命令：

`xteddy -wm -noquit`

- 让泰迪熊始终位于所有其他窗口之上：

`xteddy -float`

- 显示另一个图像 [F]ile 而不是可爱的泰迪熊：

`xteddy -F {{path/to/image}}`

- 设置泰迪熊的初始位置（`width` 和 `height` 将被忽略）：

`xteddy -geometry {{width}}x{{height}}+{{x}}+{{y}}`