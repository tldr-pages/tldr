# setx

> 设置持久的环境变量。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/setx>。

- 为当前用户设置环境变量：

`setx {{variable}} {{value}}`

- 为当前机器设置环境变量：

`setx {{variable}} {{value}} /M`

- 为远程机器上的用户设置环境变量：

`setx /s {{hostname}} /u {{username}} /p {{password}} {{variable}} {{value}}`

- 从注册表项值中设置环境变量：

`setx {{variable}} /k {{registry\key\path}}`