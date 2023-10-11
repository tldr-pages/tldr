# net

> System utility to view and modify network-related settings.
> More information: <https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/gg651155(v=ws.11)>.

- Start or stop a Windows service synchronously:

`net {{start|stop}} {{service}}`

- Make sure an SMB share is available in the current console:

`net use {{\\smb_shared_folder}} /USER:{{username}}`

- Show the folders currently shared over SMB:

`net share`

- Show who is using your SMB shares (run in elevated console):

`net session`

- Show users in a local security group:

`net localgroup "{{Administrators}}"`

- Add a user to the local security group (run in elevated console):

`net localgroup "{{Administrators}}" {{username}} /add`

- Display help for a subcommand:

`net help {{subcommand}}`

- Display help:

`net help`
