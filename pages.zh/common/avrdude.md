# avrdude

> Atmel AVR 微控制器编程的驱动程序。
> 更多信息：<https://www.nongnu.org/avrdude/user-manual/avrdude_3.html#Option-Descriptions>.

- 使用特定的 [p] 部件 ID 读取 [r] AVR 微控制器的闪存 ROM：

`avrdude -p {{part_no}} -c {{programmer_id}} -U flash:r:{{file.hex}}:i`

- 写入 AVR 微控制器的闪存 ROM：

`avrdude -p {{part_no}} -c {{programmer}} -U flash:w:{{file.hex}}`

- 列出可用的 AVR 设备：

`avrdude -p \?`

- 列出可用的 AVR 编程器：

`avrdude -c \?`
