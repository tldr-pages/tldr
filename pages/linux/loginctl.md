# loginctl

> Manage the systemd login manager.
> More information: <https://manned.org/loginctl>.

- Print the current sessions:

`loginctl list-sessions`

- Print all the properties of a specific session:

`loginctl show-session {{sessionId}} --all`

- Print the user details:

`loginctl show-user {{userName}}`

- Print specific user property:

`loginctl show-user {{userName}} --property={{propertyName}}`

- Execute `loginctl` operation remotely:

`loginctl list-users -H {{hostName}}`
