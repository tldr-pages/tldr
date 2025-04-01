# xxd

> 从二进制文件创建十六进制表示（十六进制转储），或反之。
> 更多信息：<https://manned.org/xxd>.

- 从二进制文件生成十六进制转储并显示输出：

`xxd {{input_file}}`

- 从二进制文件生成十六进制转储并保存为文本文件：

`xxd {{input_file}} {{output_file}}`

- 显示更紧凑的输出，用星号替换连续的零（如果有）：

`xxd -a {{input_file}}`

- 每列显示10个八位字节（字节）：

`xxd -c {{10}} {{input_file}}`

- 只显示前32个字节的输出：

`xxd -l {{32}} {{input_file}}`

- 以纯文本模式显示输出，列之间没有空隙：

`xxd -p {{input_file}}`

- 将纯文本十六进制转储还原为二进制，并保存为二进制文件：

`xxd -r -p {{input_file}} {{output_file}}`