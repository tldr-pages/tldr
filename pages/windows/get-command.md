# Get-Command

> List and get available commands in the current PowerShell session.
> This command can only be run through PowerShell.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/get-command>.

- List all available PowerShell commands (aliases, cmdlets, functions) in the current computer:

`Get-Command`

- List all available PowerShell commands in the current session:

`Get-Command -ListImported`

- List only PowerShell aliases/cmdlets/functions available in the computer:

`Get-Command -Type {{Alias|Cmdlet|Function}}`

- List only programs or commands available on PATH in the current session:

`Get-Command -Type Application`

- List only PowerShell commands by the module name, e.g. `Microsoft.PowerShell.Utility` for utility-related commands:

`Get-Command -Module {{module}}`

- Get the command information (e.g. version number or module name) by its name:

`Get-Command {{command}}`
