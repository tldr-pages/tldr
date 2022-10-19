# loginctl

> Manage the systemd login manager.
> More information: <https://manned.org/loginctl>.

- Print all current sessions:

`loginctl list-sessions`

- Print all properties of a specific session:

`loginctl show-session {{session_id}} --all`

- Print the details of a specific user:

`loginctl show-user {{username}}`

- Print a property of a specific user:

`loginctl show-user {{username}} --property={{property_name}}`

- Execute a `loginctl` operation on a remote host:

`loginctl list-users -H {{hostname}}`
