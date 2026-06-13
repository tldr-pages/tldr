# Get-WUSettings

> Get the current Windows Update Agent configuration. Part of external `PSWindowsUpdate` module.
> This command can only be run under PowerShell.
> More information: <https://github.com/mgajda83/PSWindowsUpdate>.

- Get the current Windows Update Agent configuration:

`Get-WUSettings`

- Send the current configuration data via email (SMTP):

`Get-WUSettings -SendReport -PSWUSettings @{SmtpServer="{{smtp_server}}"; Port={{smtp_port}} From="{{sender_email}}" To="{{receiver_email}}"}`
