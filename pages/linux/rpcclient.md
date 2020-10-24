# rpcclient

> MS-RPC client tool (part of the samba suite).
> More information: <https://www.samba.org/samba/docs/current/man-html/rpcclient.1.html>.

- Connect to a remote host:

`rpcclient --user {{domain}}\{{username}}%{{password}} {{ip}}`

- Connect to a remote host on a domain without a password:

`rpcclient --user {{username}} --workgroup {{domain}} --no-pass {{ip}}`

- Connect to a remote host, passing the password hash:

`rpcclient --user {{domain}}\{{username}} --pw-nt-hash {{ip}}`

- Execute shell commands on a remote host:

`rpcclient --user {{domain}}\{{username}}%{{password}} --command {{semicolon_separated_commands}} {{ip}}`

- Display domain users:

`rpcclient $> enumdomusers`

- Display privileges:

`rpcclient $> enumprivs`

- Display information about a specific user:

`rpcclient $> queryuser {{username|rid}}`

- Create a new user in the domain:

`rpcclient $> createdomuser {{username}}`
