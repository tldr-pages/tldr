# logoff

> Terminate a login session.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/logoff>.

- Terminate the current session:

`logoff`

- Terminate a session by its name or id:

`logoff {{session_name|session_id}}`

- Terminate a session on a specific server connected through RDP:

`logoff {{session_name|session_id}} /server:{{servername}}`
