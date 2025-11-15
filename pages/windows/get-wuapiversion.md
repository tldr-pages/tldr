# Get-WUApiVersion

> Get the Windows Update Agent version. Part of external `PSWindowsUpdate` module.
> This command can only be run under PowerShell.
> More information: <https://github.com/mgajda83/PSWindowsUpdate>.

- Get the currently-installed Windows Update Agent version:

`Get-WUApiVersion`

- Send the current configuration data via email (SMTP):

`Get-WUApiVersion -SendReport -PSWUSettings @{SmtpServer="{{smtp_server}}"; Port={{smtp_port}} From="{{sender_email}}" To="{{receiver_email}}"}`
