# systemctl list-sockets

> List active socket units currently in memory, ordered by listening address.
> See also: `systemctl list-units`, `systemctl list-unit-files`.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#list-sockets%20PATTERN%E2%80%A6>.

- List active socket units currently in memory:

`systemctl list-sockets`

- List active socket units with their socket types:

`systemctl list-sockets --show-types`

- List all socket units, including inactive and failed ones:

`systemctl list-sockets {{[-a|--all]}}`

- List socket units filtered by state:

`systemctl list-sockets --state {{active|inactive|failed|...}}`

- List socket units matching a name pattern:

`systemctl list-sockets {{pattern1 pattern2 ...}}`
