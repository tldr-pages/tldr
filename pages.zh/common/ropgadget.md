# ROPgadget

> 在二进制文件中查找 ROP 链。
> 更多信息：<https://github.com/JonathanSalwan/ROPgadget>。

- 列出二进制文件中的链：

`ROPgadget --binary {{path/to/binary}}`

- 通过正则表达式过滤二进制文件中的链：

`ROPgadget --binary {{path/to/binary}} --re {{regex}}`

- 列出二进制文件中的链，排除指定类型：

`ROPgadget --binary {{path/to/binary}} --{{norop|nojob|nosys}}`

- 在二进制文件中排除包含坏字节的链：

`ROPgadget --binary {{path/to/binary}} --badbytes {{byte_string}}`

- 列出二进制文件中长度不超过指定字节数的链：

`ROPgadget --binary {{path/to/binary}} --depth {{nbyte}}`