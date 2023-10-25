# Get-Help

> Display help information and documentation for PowerShell commands, aka. cmdlets.
> This command can only be run through PowerShell.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/get-help>.

- Display general help information for a specific cmdlet:

`Get-Help {{cmdlet}}`

- Display a more detailed documentation for a specific cmdlet:

`Get-Help {{cmdlet}} -Detailed`

- Display the full technical documentation for a specific cmdlet:

`Get-Help {{cmdlet}} -Full`

- Print only the documentation for a specific parameter of the cmdlet (use `*` to show all parameters), if available:

`Get-Help {{cmdlet}} -Parameter {{parameter}}`

- Print only the examples of the cmdlet, if available:

`Get-Help {{cmdlet}} -Examples`

- List all available cmdlet help pages:

`Get-Help *`

- Update the current help and documentation knowledge base using `Update-Help`:

`Update-Help`

- View an online version of cmdlet documentation in the default web browser:

`Get-Help {{cmdlet}} -Online`
