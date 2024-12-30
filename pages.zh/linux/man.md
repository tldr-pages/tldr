# man

> 格式化并显示手册页。
> 更多信息: <https://manned.org/man>。

- 显示命令的手册页：

`man {{command}}`

- 在浏览器中打开命令的手册页（需要设置 `BROWSER` 变量）：

`man --html {{command}}`

- 显示第 7 节的命令手册页：

`man {{7}} {{command}}`

- 列出命令的所有可用节：

`man --whatis {{command}}`

- 显示搜索手册页的路径：

`man --path`

- 显示手册页的位置，而不是手册页本身：

`man --where {{command}}`

- 使用特定语言环境显示手册页：

`man --locale {{locale}} {{command}}`

- 搜索包含搜索字符串的手册页：

`man --apropos "{{search_string}}"`