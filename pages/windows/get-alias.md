# Get-Alias

> List and get command aliases in the current PowerShell session.
> This command can only be run under PowerShell.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-alias>.

- List all aliases in the current session:

`Get-Alias`

- Get the aliased command name:

`Get-Alias {{command_alias}}`

- List all aliases assigned to a specific command:

`Get-Alias -Definition {{command}}`

- List aliases that begins with `abc`, excluding those which ends at `def`:

`Get-Alias {{abc}}* -Exclude *{{def}}`
