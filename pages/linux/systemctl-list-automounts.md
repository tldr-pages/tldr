# systemctl list-automounts

> List automount units currently in memory, showing mount paths and unit names.
> See also: `systemctl list-units`, `systemctl list-unit-files`.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#list-automounts%20PATTERN%E2%80%A6>.

- List automount units currently in memory:

`systemctl list-automounts`

- List all automount units, including inactive ones:

`systemctl list-automounts {{[-a|--all]}}`

- Filter automount units by state:

`systemctl list-automounts --state {{active|inactive|failed|...}}`

- Filter automount units by name pattern:

`systemctl list-automounts {{pattern1 pattern2 ...}}`
