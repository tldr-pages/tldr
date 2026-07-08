# net

> Tool for administration of Samba and remote CIFS servers.
> More information: <https://www.samba.org/samba/docs/current/man-html/net.8.html>.

- List shares on a Samba server:

`net rpc share list {{[-S|--server]}} {{server}} {{[-U|--user]}} {{username}}`

- Add a share to a Samba server:

`net rpc share add {{share_name}} {{path}} {{[-S|--server]}} {{server}} {{[-U|--user]}} {{username}}`

- Delete a share from a Samba server:

`net rpc share delete {{share_name}} {{[-S|--server]}} {{server}} {{[-U|--user]}} {{username}}`

- Display domain information from a remote server:

`net rpc info {{[-S|--server]}} {{server}} {{[-U|--user]}} {{username}}`

- Join an Active Directory domain:

`net ads join -U {{username%password}}`

- Display Active Directory domain information:

`net ads info`

- List user-defined shares:

`net usershare list`

- Delete a user-defined share:

`net usershare delete {{share_name}}`
