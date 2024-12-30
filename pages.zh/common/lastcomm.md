# lastcomm

> 显示最后执行的命令。
> 更多信息：<https://manpages.debian.org/latest/acct/lastcomm.1.zh.html>。

- 打印关于所有命令的记录信息：

`lastcomm`

- 显示特定用户执行的命令：

`lastcomm --user {{user}}`

- 显示系统上执行的特定命令的信息：

`lastcomm --command {{command}}`

- 显示在特定终端上执行的命令的信息：

`lastcomm --tty {{terminal_name}}`