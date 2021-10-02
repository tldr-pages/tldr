# fondue

> 可选 Windows 功能的命令行安装程序。
> 更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/fondue>.

- 启用一个指定的 Windows 功能：

`fondue /enable-feature:{{功能}}`

- 向用户隐藏所有输出信息：

`fondue /enable-feature:{{功能}} /hide-ux:all`

- 为错误报告指定调用者进程名称：

`fondue /enable-feature:{{功能}} /caller-name:{{名称}}`
