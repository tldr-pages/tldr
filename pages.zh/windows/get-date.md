# Get-Date

> 获取当前日期和时间。
> 注意：此命令只能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-date>.

- 显示当前日期和时间：

`Get-Date`

- 使用 .NET 格式说明符显示当前日期和时间：

`Get-Date -Format "{{yyyy-MM-dd HH:mm:ss}}"`

- 以 UTC 和 ISO 8601 格式显示当前日期和时间：

`(Get-Date).ToUniversalTime()`

- 转换 Unix 时间戳：

`Get-Date -UnixTimeSeconds {{1577836800}}`
