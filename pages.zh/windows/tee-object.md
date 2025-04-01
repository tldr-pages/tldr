# Tee-Object

> 将命令输出保存到文件或变量中，并同时将其发送到管道。
> 注意：此命令只能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/tee-object>.

- 将进程输出到文件和控制台：

`Get-Process | Tee-Object -FilePath {{path\to\file}}`

- 将进程输出到变量并使用 `Select-Object`：

`Get-Process notepad | Tee-Object -Variable {{proc}} | Select-Object processname,handles`