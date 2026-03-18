# net

> Administer Samba and remote CIFS servers.
> See also: `smbclient`.
> More information: <https://manned.org/net>.

- Join an Active Directory domain:

`sudo net ads join -U {{administrator}}`

- Leave an Active Directory domain:

`sudo net ads leave -U {{administrator}}`

- Display Active Directory server information:

`net ads info`

- Verify Active Directory domain membership:

`sudo net ads testjoin`

- List shares on a remote server via RPC:

`net rpc share list -S {{server_name}} -U {{username}}`

- Look up domain controllers for a domain:

`net lookup dc {{domain_name}}`

- Display the remote server's time:

`net time -S {{server_name}}`

- Display help for a subcommand:

`net help {{subcommand}}`
