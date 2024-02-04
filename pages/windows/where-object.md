# Where-Object

> Selects objects from a collection based on their property values.
> This command can only be used through PowerShell.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/where-object>.

- Filter aliases by its name:

`Get-Alias | Where-Object -{{Property}} {{Name}} -{{eq}} {{name}}`

- List all services that are currently stopped. The `$_` automatic variable represents each object that is passed to the `Where-Object` cmdlet:

`Get-Service | Where-Object {$_.Status -eq "Stopped"}`

- Use multiple conditions:

`Get-Module -ListAvailable | Where-Object { $_.Name -NotLike "Microsoft*" -And $_.Name -NotLike "PS*" }`
