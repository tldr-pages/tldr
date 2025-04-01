# Measure-Command

> 测量运行脚本块和 cmdlet 所需的时间。
> 注意：此命令只能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/measure-command>.

- 测量运行命令所需的时间：

`Measure-Command { {{command}} }`

- 将输入管道传递给 Measure-Command（传递给 `Measure-Command` 的对象在传递给 Expression 参数的脚本块中可用）：

`10, 20, 50 | Measure-Command -Expression { for ($i=0; $i -lt $_; $i++) {$i} }`
