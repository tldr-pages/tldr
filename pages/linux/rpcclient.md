# rpcclient

> MS-RPC client tool (part of the samba suite).
> More information: <https://www.samba.org/samba/docs/current/man-html/rpcclient.1.html>.

- Connect to a host:

`rpcclient --user {{domain}}\{{username}}%{{password}} {{ip}}`

- Connect to a host on a domain without a password:

`rpcclient --user {{username}} --workgroup {{domain}} --no-pass {{ip}}`

- Connect to a host, passing the password hash:

`rpcclient --user {{domain}}\{{username}} --pw-nt-hash {{ip}}`

- Display domain users:

`rpcclient $> enumdomusers`

- Display domain groups:

`rpcclient $> enumdomgroups`

- Display privileges:

`rpcclient $> enumprivs`

- Display information about a specific user:

`rpcclient $> queryuser {{username|rid}}`

- Create a new user in the domain:

`rpcclient $> createdomuser {{username}}`
