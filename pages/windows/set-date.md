# Set-Date

> Changes the system time on the computer to a time that you specify.
> This command can only be used through PowerShell.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/set-date>.

- Add three days to the system date:

`Set-Date -Date (Get-Date).AddDays({{3}})`

- Set the system clock back 10 minutes:

`Set-Date -Adjust -0:10:0 -DisplayHint Time`

- Add 90 minutes to the system clock:

`$90mins = New-TimeSpan -Minutes {{90}}; Set-Date -Adjust $90mins`
