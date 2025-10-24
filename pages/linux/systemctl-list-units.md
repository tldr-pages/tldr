# systemctl list-units

> List units that systemd currently has in memory.
> See also: `systemctl list-unit-files` for listing installed unit files.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#list-units%20PATTERN%E2%80%A6>.

- List units which are active, have pending jobs, or have failed:

`systemctl list-units`

- List all units, including inactive ones:

`systemctl list-units {{[-a|--all]}}`

- Filter by unit type:

`systemctl list-units {{[-t|--type]}} {{service|socket|timer|...}}`

- Filter by state:

`systemctl list-units --state {{running|listening|dead|...}}`

- Filter by a name pattern:

`systemctl list-units 'systemd*'`

- Print output directly to `stdout`:

`systemctl list-units --no-pager`

- Print output without headers or footers (for scripts):

`systemctl list-units --no-legend`
