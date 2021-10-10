# hexdump

> 一个 ASCII，十进制，十六进制，八进制转换查看工具。
> 更多信息：<https://manned.org/hexdump>.

- 打印文件的十六进制表示形式：

`hexdump {{文件}}`

- 以十六进制显示输入偏移量，并在最后两列中显示其 ASCII 表示形式：

`hexdump -C {{文件}}`

- 显示文件的十六进制表示，但只解释输入的 N 个字节：

`hexdump -C -n{{字节数}} {{文件}}`
