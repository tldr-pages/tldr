# compgen

> Bash中的一个内置命令，用于自动补全，在按下TAB键两次时调用。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-compgen>。

- 列出所有可以运行的命令：

`compgen -c`

- 列出以指定字符串开头的所有可以运行的命令：

`compgen -c {{str}}`

- 列出所有别名：

`compgen -a`

- 列出所有可以运行的函数：

`compgen -A function`

- 显示shell保留关键字：

`compgen -k`

- 查看以'ls'开头的所有可用命令/别名：

`compgen -ac {{ls}}`