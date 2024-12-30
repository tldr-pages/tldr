# hexdump

> 一个 ASCII、十进制、十六进制和八进制的转储。
> 更多信息：<https://manned.org/hexdump>。

- 打印文件的十六进制表示，重复的行用 '*' 替代：

`hexdump {{path/to/file}}`

- 以两列显示输入偏移量的十六进制和其 ASCII 表示：

`hexdump -C {{path/to/file}}`

- 打印文件的十六进制表示，但只解释输入的 n 个字节：

`hexdump -C -n{{number_of_bytes}} {{path/to/file}}`

- 不用 '*' 替代重复的行：

`hexdump --no-squeezing {{path/to/file}}`