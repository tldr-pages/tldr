# xteddy

> 一个可爱的泰迪熊，用于您的 X Windows 桌面。
> 更多信息：<https://manned.org/xteddy>.

- 在 X 桌面上显示一个可爱的泰迪熊：

`xteddy`

- 使用窗口管理器显示泰迪熊，并忽略“退出”（`q`）命令：

`xteddy -wm -noquit`

- 让泰迪熊始终位于所有其他窗口之上：

`xteddy -float`

- 显示另一个图像 [文]件而不是可爱的泰迪熊：

`xteddy -F {{path/to/image}}`

- 设置泰迪熊的初始位置（`width` 和 `height` 被忽略）：

`xteddy -geometry {{width}}x{{height}}+{{x}}+{{y}}`
