# rpcclient

> MS-RPC client tool (part of the samba suite).
> More information: <https://www.samba.org/samba/docs/current/man-html/rpcclient.1.html>.

- Connect to a remote host:

`rpcclient {{[-U|--user]}} {{domain}}\{{username}}%{{password}} {{ip_address}}`

- Connect to a remote host on a domain without a password:

`rpcclient {{[-U|--user]}} {{username}} {{[-W|--workgroup]}} {{domain}} {{[-N|--no-pass]}} {{ip_address}}`

- Connect to a remote host, passing the password hash:

`rpcclient {{[-U|--user]}} {{domain}}\{{username}} --pw-nt-hash {{ip_address}}`

- Execute shell commands on a remote host:

`rpcclient {{[-U|--user]}} {{domain}}\{{username}}%{{password}} {{[-c|--command]}} {{semicolon_separated_commands}} {{ip_address}}`

- Display domain users:

`enumdomusers`

- Display privileges:

`enumprivs`

- Display information about a specific user:

`queryuser {{username|rid}}`

- Create a new user in the domain:

`createdomuser {{username}}`
