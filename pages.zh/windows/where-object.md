# Where-Object

> 根据对象的属性值从集合中选择对象。
> 注意：此命令只能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.core/where-object>.

- 按名称过滤别名：

`Get-Alias | Where-Object -{{Property}} {{Name}} -{{eq}} {{name}}`

- 列出所有当前已停止的服务。`$_` 自动变量代表传递给 `Where-Object` cmdlet 的每个对象：

`Get-Service | Where-Object {$_.Status -eq "Stopped"}`

- 使用多个条件：

`Get-Module -ListAvailable | Where-Object { $_.Name -NotLike "Microsoft*" -And $_.Name -NotLike "PS*" }`
