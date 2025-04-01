# Start-Service

> 启动已停止的服务。
> 注意：此命令只能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.management/start-service>.

- 使用服务名称启动服务：

`Start-Service -Name {{service_name}}`

- 显示信息但不启动服务：

`Start-Service -DisplayName *{{name}}* -WhatIf`

- 启动已禁用的服务：

`Set-Service {{service_name}} -StartupType {{manual}}; Start-Service {{service_name}}`