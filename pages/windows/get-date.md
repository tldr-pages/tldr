# Get-Date

> Get the current date and time.
> Note: This command can only be used through PowerShell.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-date>.

- Display the current date and time:

`Get-Date`

- Display the current date and time with a .NET format specifier:

`Get-Date -Format "{{yyyy-MM-dd HH:mm:ss}}"`

- Display the current date and time in UTC and ISO 8601 format:

`(Get-Date).ToUniversalTime()`

- Convert a Unix timestamp:

`Get-Date -UnixTimeSeconds {{1577836800}}`
