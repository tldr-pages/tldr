# Wait-Process

> Waits for the processes to be stopped before accepting more input.
> Note: This command can only be used through PowerShell.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/wait-process>.

- Stop a process and wait:

`Stop-Process -Id {{process_id}}; Wait-Process -Id {{process_id}}`

- Wait for processes for a specified time:

`Wait-Process -Name {{process_name}} -Timeout {{30}}`
