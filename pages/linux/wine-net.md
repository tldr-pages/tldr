# wine net

> Start, stop, and list Windows services in a Wine prefix.
> A reimplementation of a subset of the Windows `net` command.
> More information: <https://gitlab.winehq.org/wine/wine/-/wikis/Commands>.

- List the currently running services:

`wine net start`

- Start a specific service:

`wine net start {{service_name}}`

- Stop a running service:

`wine net stop {{service_name}}`

- List the current network connections:

`wine net use`

- Display help:

`wine net help`
