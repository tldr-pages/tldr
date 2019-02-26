# compgen

> 用于在bash中自动完成的内置命令,按两次tab键即可调用该命令.

- 显示所有可以执行的命令:

`compgen -c`

- 列出所有别名:

`compgen -a`

- 列出所有可以运行的函数:

`compgen -A function`

- 列出所有shell的保留关键字:

`compgen -k`

- 查看以 'ls' 开头的所有可用命令和别名:

`compgen -ac {{ls}}`
