# Set-Alias

> A powershell command to set or modify alias.
> Note: `sal` can be used as an alias for `Set-Alias`.
> More information: <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/set-alias>.

- Create or reassign new alias:

`Set-Alias -Name {{text}} -Value {{command}}`

- Add a description to alias:

`Set-Alias -Name {{text}} -Value {{command}} -Description "{{description}}"`
