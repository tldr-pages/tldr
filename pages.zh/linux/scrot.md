# scrot

> 屏幕截图工具。
> 更多信息：<https://github.com/resurrecting-open-source-projects/scrot>。

- 捕获屏幕截图并将其保存到当前目录，文件名为当前日期：

`scrot`

- 捕获屏幕截图并将其保存为 `capture.png`：

`scrot {{capture.png}}`

- 交互式捕获屏幕截图：

`scrot --select`

- 交互式捕获屏幕截图，按键盘输入时不退出，按 `ESC` 键退出：

`scrot --select --ignorekeyboard`

- 交互式捕获屏幕截图，通过彩色线条划定区域：

`scrot --select --line color={{x11_color|rgb_color}}`

- 从当前聚焦的窗口捕获屏幕截图：

`scrot --focused`

- 在拍摄屏幕截图之前显示10秒的倒计时：

`scrot --count --delay {{10}}`