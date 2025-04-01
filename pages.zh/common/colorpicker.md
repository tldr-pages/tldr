# colorpicker

> 一个极简的 X11 颜色选择器。
> 除 `<左键>` 外的任何鼠标操作都将退出程序。
> 更多信息：<https://github.com/ym1234/colorpicker>。

- 启动 colorpicker 并将每次点击的像素的十六进制和 RGB 值打印到 `stdout`：

`colorpicker`

- 只打印一次点击的像素颜色，然后退出：

`colorpicker --one-shot`

- 打印每次点击的像素颜色，并在按下键时退出：

`colorpicker --quit-on-keypress`

- 只打印 RGB 值：

`colorpicker --rgb`

- 只打印十六进制值：

`colorpicker --hex`
