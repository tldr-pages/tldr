# scrot

> 屏幕捕获工具。
> 更多信息：<https://github.com/resurrecting-open-source-projects/scrot>。

- 捕获屏幕截图并将其保存到当前目录，文件名使用当前日期：

`scrot`

- 捕获屏幕截图并将其保存为 `capture.png`：

`scrot {{capture.png}}`

- 交互式捕获屏幕截图：

`scrot --select`

- 交互式捕获屏幕截图，不因键盘输入而退出，按 `<Esc>` 退出：

`scrot --select --ignorekeyboard`

- 交互式捕获屏幕截图，使用彩色线指定区域：

`scrot --select --line color={{x11_color|rgb_color}}`

- 从当前聚焦的窗口捕获屏幕截图：

`scrot --focused`

- 在捕获屏幕截图前显示 10 秒倒计时：

`scrot --count --delay {{10}}`
