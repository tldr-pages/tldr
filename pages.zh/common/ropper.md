# ropper

> 在二进制文件中查找 ROP 小工具。
> 更多信息：<https://scoding.de/ropper/>.

- 列出二进制文件中的小工具：

`ropper --file {{path/to/binary}}`

- 通过正则表达式过滤二进制文件中的小工具：

`ropper --file {{path/to/binary}} --search {{regex}}`

- 列出二进制文件中特定类型的小工具：

`ropper --file {{path/to/binary}} --type {{rop|job|sys|all}}`

- 排除二进制文件中的坏字节小工具：

`ropper --file {{path/to/binary}} --badbytes {{byte_string}}`

- 列出二进制文件中指定指令计数的小工具：

`ropper --file {{path/to/binary}} --inst-count {{count}}`