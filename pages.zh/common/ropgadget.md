# ROPgadget

> 在二进制文件中查找ROP小工具。
> 更多信息：<https://github.com/JonathanSalwan/ROPgadget>。

- 列出二进制文件中的小工具：

`ROPgadget --binary {{path/to/binary}}`

- 按正则表达式过滤二进制文件中的小工具：

`ROPgadget --binary {{path/to/binary}} --re {{regex}}`

- 列出二进制文件中的小工具，排除指定类型：

`ROPgadget --binary {{path/to/binary}} --{{norop|nojob|nosys}}`

- 排除二进制文件中的坏字节小工具：

`ROPgadget --binary {{path/to/binary}} --badbytes {{byte_string}}`

- 列出二进制文件中指定字节数以内的小工具：

`ROPgadget --binary {{path/to/binary}} --depth {{nbyte}}`