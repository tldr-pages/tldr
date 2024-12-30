# 火锅

> 安装可选的 Windows 功能。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/fondue>。

- 启用特定的 Windows 功能：

`fondue /enable-feature:{{feature}}`

- 将所有输出消息隐藏给用户：

`fondue /enable-feature:{{feature}} /hide-ux:all`

- 指定用于错误报告的调用进程名称：

`fondue /enable-feature:{{feature}} /caller-name:{{name}}`