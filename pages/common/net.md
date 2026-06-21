# net

> Tool for administering Samba and remote CIFS servers.
> See also: `smbclient`, `smbpasswd`.
> More information: <https://www.samba.org/samba/docs/current/man-html/net.8.html>.

- Join an Active Directory domain:

`net ads join -U {{username}}`

- Leave an Active Directory domain:

`net ads leave -U {{username}}`

- Test whether the machine is successfully joined to a domain:

`net ads testjoin`

- List shares on a remote server:

`net rpc share list -S {{server}} -U {{username}}`

- Add a user-defined share:

`net usershare add {{sharename}} {{/path/to/directory}} "{{Comment}}"`

- List user-defined shares:

`net usershare list`

- Display the current time on a remote server:

`net time -S {{server}}`

- Look up the IP address of a NetBIOS name:

`net lookup {{hostname}}`
