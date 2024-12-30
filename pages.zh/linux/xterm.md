# xterm

> X窗口系统的终端仿真器。
> 更多信息：<https://manned.org/xterm>。

- 打开标题为 `Example` 的终端：

`xterm -T {{Example}}`

- 以全屏模式打开终端：

`xterm -fullscreen`

- 打开背景为深蓝色，前景（字体颜色）为黄色的终端：

`xterm -bg {{darkblue}} -fg {{yellow}}`

- 打开每行100个字符和35行，屏幕位置为x=200px，y=20px的终端：

`xterm -geometry {{100}}x{{35}}+{{200}}+{{20}}`

- 使用Serif字体和字体大小为20打开终端：

`xterm -fa {{'Serif'}} -fs {{20}}`