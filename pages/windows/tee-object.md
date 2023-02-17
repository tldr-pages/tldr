# Tee-Object

> Saves command output in a file or variable and also sends it down the pipeline.
> This command can only be used through PowerShell.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/tee-object>.

- Output processes to a file and to the console:

`Get-Process | Tee-Object -FilePath {{path\to\file}}`

- Output processes to a variable and `Select-Object`:

`Get-Process notepad | Tee-Object -Variable {{proc}} | Select-Object processname,handles`
