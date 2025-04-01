# Set-Service

> 启动、停止和暂停服务，以及更改服务属性。
> 注意：此命令只能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.management/set-service>.

- 更改显示名称：

`Set-Service -Name {{hostname}} -DisplayName "{{name}}"`

- 更改服务的启动类型：

`Set-Service -Name {{service_name}} -StartupType {{Automatic}}`

- 更改服务的描述：

`Set-Service -Name {{service_name}} -Description "{{description}}"`