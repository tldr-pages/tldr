# avrdude

> 用于 Atmel AVR 微控制器编程的驱动程序。
> 更多信息：<https://www.nongnu.org/avrdude/user-manual/avrdude_3.html#Option-Descriptions>.

- 使用指定的 [p]art ID 读[r]取 AVR 微控制器的闪存 ROM：

`avrdude -p {{部件编号}} -c {{编程器 ID}} -U flash:r:{{文件.hex}}:i`

- 向 AVR 微控制器的闪存 ROM 写[w]入数据：

`avrdude -p {{部件编号}} -c {{编程器}} -U flash:w:{{文件.hex}}`

- 列出可用的 AVR 设备：

`avrdude -p \?`

- 列出可用的 AVR 编程器：

`avrdude -c \?`
