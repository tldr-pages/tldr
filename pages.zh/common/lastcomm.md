# lastcomm

> 显示最后执行的命令。
> 更多信息：<https://manpages.debian.org/latest/acct/lastcomm.1.en.html>。

- 打印 acct（记录文件）中所有命令的信息：

`lastcomm`

- 显示由指定用户执行的命令：

`lastcomm --user {{user}}`

- 显示在系统上执行的指定命令的信息：

`lastcomm --command {{command}}`

- 显示在指定终端上执行的命令的信息：

`lastcomm --tty {{terminal_name}}`
