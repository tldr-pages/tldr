# loginctl

> Manage the systemd login manager.
> More information: <https://www.freedesktop.org/software/systemd/man/loginctl.html>.

- Print all current sessions:

`loginctl list-sessions`

- Print all properties of a specific session:

`loginctl show-session {{session_id}} {{[-a|--all]}}`

- Print all properties of a specific user:

`loginctl show-user {{username}}`

- Print a specific property of a user:

`loginctl show-user {{username}} {{[-p|--property]}} {{property_name}}`

- Execute a `loginctl` operation on a remote host:

`loginctl list-users {{[-H|--host]}} {{hostname}}`

- Log a user out on all of their sessions:

`loginctl terminate-user {{username}}`

- Display help:

`loginctl {{[-h|--help]}}`
