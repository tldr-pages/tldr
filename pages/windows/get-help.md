# Get-Help

> Display help information and documentation for PowerShell commands (aliases, cmdlets, and functions).
> This command can only be run through PowerShell.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/get-help>.

- Display general help information for a specific PowerShell command:

`Get-Help {{command}}`

- Display a more detailed documentation for a specific PowerShell command:

`Get-Help {{command}} -Detailed`

- Display the full technical documentation for a specific PowerShell command:

`Get-Help {{command}} -Full`

- Print only the documentation for a specific parameter of the PowerShell command (use `*` to show all parameters), if available:

`Get-Help {{command}} -Parameter {{parameter}}`

- Print only the examples of the cmdlet, if available:

`Get-Help {{command}} -Examples`

- List all available cmdlet help pages:

`Get-Help *`

- Update the current help and documentation knowledge base using `Update-Help`:

`Update-Help`

- View an online version of PowerShell command documentation in the default web browser:

`Get-Help {{command}} -Online`
