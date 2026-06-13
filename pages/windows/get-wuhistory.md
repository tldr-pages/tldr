# Get-WUHistory

> Get the history of installed updates from Windows Update. Part of external `PSWindowsUpdate` module.
> This command can only be run under PowerShell.
> More information: <https://github.com/mgajda83/PSWindowsUpdate>.

- Get list of update history:

`Get-WUHistory`

- List the last 10 installed updates:

`Get-WUHistory -Last {{10}}`

- List all updates installed from a specific date to today:

`Get-WUHistory -MaxDate {{date}}`

- List all updates installed in the past 24 hours:

`Get-WUHistory -MaxDate (Get-Date).AddDays(-1)`

- Send the results via email (SMTP):

`Get-WUHistory -SendReport -PSWUSettings @{SmtpServer="{{smtp_server}}"; Port={{smtp_port}} From="{{sender_email}}" To="{{receiver_email}}"}`
