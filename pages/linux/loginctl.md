# loginctl

> Manage the systemd login manager.
> More information: <https://manned.org/loginctl>.

- Print all current sessions:

`loginctl list-sessions`

- Print all properties of a specific session:

`loginctl show-session {{sessionId}} --all`

- Print the details of a specific user:

`loginctl show-user {{userName}}`

- Print specific user property:

`loginctl show-user {{userName}} --property={{propertyName}}`

- Execute a `loginctl` operation on a remote host:

`loginctl list-users -H {{hostName}}`
