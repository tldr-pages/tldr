# command

> Command 强制当前 shell 执行指定程序，并忽略具有相同名称的任何函数、内置函数和别名。
> 更多信息：<https://manned.org/command>.

- 从字面上执行 `ls` 程序，即使存在 `ls` 别名：

`command {{ls}}`

- 显示指定命令的可执行程序路径或别名定义：

`command -v {{命令名}}`
