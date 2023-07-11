# net

> System utility to view and modify network-related settings
> More information: <https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/gg651155(v=ws.11)>.

- Remote filesystem (IPC$)

`net use \\{IP}`

- List current SMB shares

`net share`

- Who is using your network shares (elevated)

`net session`

- List local Administrators

`net localgroup "Administrators"`

- Add user to the administrators group (elevated)

`net localgroup "Administrators" {{user}} /add`

- Start and stop windows services syncronously:

`net {{start|stop}} {{service_name}}`
