# logoff

> Terminate a login session.

- Terminate the current session:

`logoff`

- Terminate a session by its name or id:

`logoff {{session_name|session_id}}`

- Terminate a session on a specific server connected through RDP:

`logoff {{session_name|session_id}} /server:{{servername}}`

- Terminate a session within a server or virtual machine (session id is required):

`logoff /vm {{session_id}}`
