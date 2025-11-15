# systemctl whoami

> Show units that processes belong to.
> If no PID is specified, shows the unit the `systemctl` command itself is invoked in.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#whoami%20%5BPID%E2%80%A6%5D>.

- Show the unit of the current shell (where `systemctl` is running):

`systemctl whoami`

- Show the unit of the current shell in user service manager (services managed for your login session):

`systemctl whoami --user`

- Show the unit a specific process belongs to:

`systemctl whoami {{pid}}`

- Show the units for multiple processes:

`systemctl whoami {{pid1 pid2 ...}}`
