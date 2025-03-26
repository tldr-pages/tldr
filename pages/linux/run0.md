# run0

> Elevate privileges interactively.
> Similar to `sudo`, but it's not a SUID binary, authentication takes place via polkit, and commands are invoked from a `systemd` service.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/run0.html>.

- Run a command as root:

`run0 {{command}}`

- Run a command as another user and/or group:

`run0 {{[-u|--user]}} {{username|uid}} {{[-g|--group]}} {{group_name|gid}} {{command}}`
