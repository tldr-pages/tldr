# net

> Samba/CIFS network administration and RPC client for Windows domains.
> More information: <https://www.samba.org/samba/docs/current/man-html/net.8.html>.

- Display general help or help for specific command:

`net {{help}} {{[command]}}`

- List all available shares on local/remote Samba server:

`net {{share}}`

- Mount/connect to remote SMB/CIFS share (Windows-style):

`net use {{\\\\server\\share}} {{[password]}}`

- List all domain users (or info for specific user):

`net {{user}} {{list}} {{[username]}}`

- List all domain groups (or members of specific group):

`net {{group}} {{list}} {{[groupname]}}`

- Join current machine to Active Directory domain:

`net {{ads join}} {{[-U|--user]}} {{DOMAIN\\\\admin}}`

- Show domain/workgroup membership and configuration:

`net {{ads info}}`

- List open files on server (optionally close specific file ID):

`net {{file}} {{[close {id}]}}`

- List active SMB sessions/connections to server:

`net {{session}}`
