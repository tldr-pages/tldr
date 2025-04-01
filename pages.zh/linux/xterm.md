# xterm

> X Window 系统的终端模拟器。
> 更多信息：<https://manned.org/xterm>。

- 打开标题为 `Example` 的终端：

`xterm -T {{Example}}`

- 以全屏模式打开终端：

`xterm -fullscreen`

- 以深蓝色背景和黄色前景（字体颜色）打开终端：

`xterm -bg {{darkblue}} -fg {{yellow}}`

- 以每行 100 个字符，共 35 行，屏幕位置 x=200 像素，y=20 像素打开终端：

`xterm -geometry {{100}}x{{35}}+{{200}}+{{20}}`

- 使用 Serif 字体，字体大小为 20 打开终端：

`xterm -fa {{'Serif'}} -fs {{20}}`
