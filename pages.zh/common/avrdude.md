# avrdude

> Atmel AVR 微控制器的驱动程序。
> 更多信息：<https://www.nongnu.org/avrdude/user-manual/avrdude_3.html#Option-Descriptions>。

- 读取具有特定部件 ID 的 AVR 微控制器的闪存 ROM：

`avrdude -p {{部件_id}} -c {{编程器_id}} -U flash:r:{{文件.hex}}:i`

- 写入 AVR 微控制器的闪存 ROM：

`avrdude -p {{部件_id}} -c {{编程器}} -U flash:w:{{文件.hex}}`

- 列出可用的 AVR 设备：

`avrdude -p \?`

- 列出可用的 AVR 编程器：

`avrdude -c \?`
