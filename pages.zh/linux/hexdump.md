# hexdump

> 用于生成文件的ASCII、十进制、十六进制、八进制转储。
> 更多信息：<https://manned.org/hexdump>。

- 打印文件的十六进制表示，用 '*' 替换重复的行：

`hexdump {{path/to/file}}`

- 以两列显示输入偏移量的十六进制表示及其ASCII表示：

`hexdump {{[-C|--canonical]}} {{path/to/file}}`

- 显示文件的十六进制表示，但只解释输入的前 n 个字节：

`hexdump {{[-C|--canonical]}} {{[-n|--length]}} {{number_of_bytes}} {{path/to/file}}`

- 不用 '*' 替换重复的行：

`hexdump {{[-v|--no-squeezing]}} {{path/to/file}}`