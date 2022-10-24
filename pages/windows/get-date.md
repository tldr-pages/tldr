# Get-Date

> Gets the current date and time.
> This command can only be used through PowerShell.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-date>.

- Get the current date and time:

`Get-Date`

- Get the date and time with a .NET format specifier:

`Get-Date -Format {{"dddd MM/dd/yyyy HH:mm K"}}`

- Convert the current time to UTC time:

`(Get-Date).ToUniversalTime()`

- Convert a Unix timestamp:

`Get-Date -UnixTimeSeconds {{1577836800}}`
