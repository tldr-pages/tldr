# Out-String

> Outputs input objects as a string.
> This command can only be used through PowerShell.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/out-string>.

- Print host information as string:

`Get-Alias | Out-String`

- Convert each object to a string rather than concatenating all the objects into a single string:

`Get-Alias | Out-String -Stream`

- Use the `Width` parameter to prevent truncation:

`@{TestKey = ('x' * 200)} | Out-String -Width {{250}}`
