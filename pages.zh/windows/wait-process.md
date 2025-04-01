# Wait-Process

> 等待指定的进程停止后再接受更多的输入。
> 注意：此命令只能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.management/wait-process>.

- 停止一个进程并等待：

`Stop-Process -Id {{process_id}}; Wait-Process -Id {{process_id}}`

- 等待指定时间内的进程：

`Wait-Process -Name {{process_name}} -Timeout {{30}}`