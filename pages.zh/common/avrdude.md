# avrdude

> Atmel AVR 微控制器编程的驱动程序。
> 更多信息：<https://www.nongnu.org/avrdude/>.

- [r]ead 具有特定 [p]art ID 的 AVR 微控制器的闪存 ROM：

`avrdude -p {{part_no}} -c {{programmer_id}} -U flash:r:{{file.hex}}:i`

- [w]rite 到闪存 ROM AVR 微控制器：

`avrdude -p {{part_no}} -c {{programmer}} -U flash:w:{{file.hex}}`

- 列出可用的 AVR 设备：

`avrdude -p \?`

- 列出可用的 AVR 编程器：

`avrdude -c \?`