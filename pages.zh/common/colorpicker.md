# 颜色选择器

> 一个简约的 X11 颜色选择器。
> 除左键点击外的任何鼠标手势将退出程序。
> 更多信息：<https://github.com/ym1234/colorpicker>。

- 启动颜色选择器并将每个被点击像素的十六进制和 RGB 值打印到 `stdout`：

`colorpicker`

- 仅打印一个被点击像素的颜色，然后退出：

`colorpicker --one-shot`

- 打印每个被点击像素的颜色，并在按下任意键时退出：

`colorpicker --quit-on-keypress`

- 仅打印 RGB 值：

`colorpicker --rgb`

- 仅打印十六进制值：

`colorpicker --hex`