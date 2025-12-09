# systemctl status

> Display the status of systemd units.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#status%20PATTERN%E2%80%A6%7CPID%E2%80%A6%5D>.

- Show the status of a systemd unit:

`systemctl status {{unit}}.{{service|timer|socket|target|...}}`

- Show the status of failed units:

`systemctl status --failed`

- List all running services:

`systemctl status`

- List all units in the system:

`systemctl status --all`

- List all units of a specific type:

`systemctl status --type {{service|timer|socket|target|...}}`

- List all units with a specific state:

`systemctl status --state {{active|inactive|failed}}`

- Show the status of a user unit:

`systemctl status {{unit}} --user`
