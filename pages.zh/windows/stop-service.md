# Stop-Service

> 停止正在运行的服务。
> 注意：此命令只能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.management/stop-service>.

- 停止本地计算机上的服务：

`Stop-Service -Name {{service_name}}`

- 使用显示名称停止服务：

`Stop-Service -DisplayName "{{name}}"`

- 强制停止具有依赖服务的服务，并在停止前确认：

`Stop-Service -Name {{service_name}} -Force -Confirm`