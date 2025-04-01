# ropper

> 在二进制文件中查找 ROP 小工具。
> 更多信息：<https://scoding.de/ropper/>.

- 列出二进制文件中的小工具：

`ropper --file {{path/to/binary}}`

- 通过正则表达式筛选二进制文件中的小工具：

`ropper --file {{path/to/binary}} --search {{regex}}`

- 列出二进制文件中指定类型的小工具：

`ropper --file {{path/to/binary}} --type {{rop|job|sys|all}}`

- 排除二进制文件中包含指定坏字节的小工具：

`ropper --file {{path/to/binary}} --badbytes {{byte_string}}`

- 列出二进制文件中指令数量不超过指定数量的小工具：

`ropper --file {{path/to/binary}} --inst-count {{count}}`
