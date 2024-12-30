# man

> 格式化并显示手册页。
> 更多信息：<https://manned.org/man>。

- 显示命令的手册页：

`man {{command}}`

- 显示第7节的命令手册页：

`man {{7}} {{command}}`

- 列出命令的所有可用节：

`man -f {{command}}`

- 显示搜索手册页的路径：

`man --path`

- 显示手册页的位置，而不是手册页本身：

`man -w {{command}}`

- 使用特定的语言环境显示手册页：

`man {{command}} --locale={{locale}}`

- 搜索包含搜索字符串的手册页：

`man -k "{{search_string}}"`