# Measure-Command

> Measures the time it takes to run script blocks and cmdlets.
> This command can only be used through PowerShell.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/measure-command>.

- Measure the time it takes to run a command:

`Measure-Command { {{command}} }`

- Pipe input to Measure-Command (objects that are piped to `Measure-Command` are available to the script block that is passed to the Expression parameter):

`10, 20, 50 | Measure-Command -Expression { for ($i=0; $i -lt $_; $i++) {$i} }`
