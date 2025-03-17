# man

> 展示手册分页 (manual page).
> 更多信息：<https://manned.org/man>.

- 展示一条命令的使用手册分页:

`man {{command}}`

- 从第七章节展示一条命令的使用手册分页:

`man {{7}} {{command}}`

- 列表展示一条命令的所有可用章节:

`man -f {{command}}`

- 展示搜索手册分页的路径:

`man --path`

- 展示使用手册分页的位置, 而不是手册分页本身:

`man -w {{command}}`

- 使用特定的语言来展示使用手册分页:

`man {{command}} --locale={{locale}}`

- 搜索包含搜索字符串的手册页:

`man -k "{{search_string}}"`
