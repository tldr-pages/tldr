# 命令

> 命令强制 shell 执行程序，并忽略任何同名的函数、内置命令和别名。
> 更多信息：<https://manned.org/command>。

- 字面上执行 `ls` 程序，即使存在 `ls` 别名：

`command {{ls}}`

- 显示特定命令的可执行文件路径或别名定义：

`command -v {{command_name}}`