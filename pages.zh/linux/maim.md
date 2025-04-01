# maim

> 屏幕截图工具。
> 更多信息：<https://github.com/naelstrof/maim>。

- 捕获屏幕截图并保存到指定路径：

`maim {{path/to/screenshot.png}}`

- 捕获选定区域的屏幕截图：

`maim --select {{path/to/screenshot.png}}`

- 捕获选定区域的屏幕截图并保存到剪贴板（需要 `xclip`）：

`maim --select | xclip -selection clipboard -target image/png`

- 捕获当前活动窗口的屏幕截图（需要 `xdotool`）：

`maim --window $(xdotool getactivewindow) {{path/to/screenshot.png}}`
