# command

> 命令强制 shell 执行命令程序，并忽略具有相同名称的任何函数、内置函数和别名（会忽略掉一切别名，执行命令本身）。
> 更多信息：<https://manned.org/command>.

- 从字面上执行 `ls` 程序，即使存在 ls 别名：

`command {{ls}}`
