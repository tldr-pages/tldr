# xxd

> 从二进制文件创建十六进制表示（十六进制转储），或反之亦然。
> 更多信息：<https://manned.org/xxd>。

- 从二进制文件生成十六进制转储并显示输出：

`xxd {{input_file}}`

- 从二进制文件生成十六进制转储并将其保存为文本文件：

`xxd {{input_file}} {{output_file}}`

- 显示更紧凑的输出，用星号替换连续的零（如果有的话）：

`xxd -a {{input_file}}`

- 按每列一个八位字节（字节）显示10列输出：

`xxd -c {{10}} {{input_file}}`

- 输出长度限制为32个字节：

`xxd -l {{32}} {{input_file}}`

- 以普通模式显示输出，列之间没有任何间隔：

`xxd -p {{input_file}}`

- 将明文十六进制转储恢复为二进制，并将其保存为二进制文件：

`xxd -r -p {{input_file}} {{output_file}}`