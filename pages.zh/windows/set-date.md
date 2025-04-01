# Set-Date

> 将计算机的系统时间更改为指定的时间。
> 注意：此命令只能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/set-date>。

- 将系统日期增加三天：

`Set-Date -Date (Get-Date).AddDays({{3}})`

- 将系统时钟回调 10 分钟：

`Set-Date -Adjust -0:10:0 -DisplayHint Time`

- 将系统时钟增加 90 分钟：

`$90mins = New-TimeSpan -Minutes {{90}}; Set-Date -Adjust $90mins`