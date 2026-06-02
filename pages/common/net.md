# net

> Administer Samba and remote CIFS servers.
> More information: <https://www.samba.org/samba/docs/current/man-html/net.8.html>.

- List available shares on a server:

`net rpc share list {{[-S|--server]}} {{server}} {{[-U|--user]}} {{domain/username}}`

- List local user-defined shares:

`net usershare list`

- Display information about a local user-defined share:

`net usershare info {{share_name}}`

- Add a local user-defined share:

`net usershare add {{share_name}} {{path/to/directory}} "{{comment}}" {{acl}} {{guest_ok|guest_not_ok}}`

- Delete a local user-defined share:

`net usershare delete {{share_name}}`

- List users in a domain:

`net {{[ads|rpc]}} user {{[-U|--user]}} {{domain/username}}`
