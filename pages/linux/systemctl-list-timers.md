# systemctl list-timers

> List all active systemd timers.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#list-timers%20PATTERN…>.

- List all active timers:

`systemctl list-timers`

- List all timers, including inactive ones:

`systemctl list-timers {{[-a|--all]}}`

- List timers matching a pattern:

`systemctl list-timers {{pattern}}`

- List timers matching a specific state (e.g., active, failed):

`systemctl list-timers --state {{state}}`
