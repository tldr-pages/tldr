# setx

> 设置持久环境变量。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/setx>.

- 为当前用户设置环境变量：

`setx {{variable}} {{value}}`

- 为当前计算机设置环境变量：

`setx {{variable}} {{value}} /M`

- 为远程计算机上的用户设置环境变量：

`setx /s {{hostname}} /u {{username}} /p {{password}} {{variable}} {{value}}`

- 从注册表键值设置环境变量：

`setx {{variable}} /k {{registry\key\path}}`
