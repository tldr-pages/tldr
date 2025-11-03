# systemctl list-timers

> List all active systemd timers.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#list-timers%20PATTERN%E2%80%A6>.

- List all active timers:

`systemctl list-timers`

- List all timers, including inactive ones:

`systemctl list-timers {{[-a|--all]}}`

- List timers matching a pattern:

`systemctl list-timers {{pattern}}`

- List timers matching a specific state:

`systemctl list-timers --state {{active|inactive|failed|...}}`
