# systemctl list-units

> List units that systemd currently has in memory.
> See also: `systemctl list-unit-files` for listing installed unit template files.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#list-units%20PATTERN%E2%80%A6>.

- List units which are active, have pending jobs, or have failed (default):

`systemctl list-units`

- List all units, including inactive ones:

`systemctl list-units --all`

- Filter by unit type (e.g., service):

`systemctl list-units --type service`

- Filter by state (e.g., running):

`systemctl list-units --state running`

- Filter by a name pattern (e.g., systemd*):

`systemctl list-units 'systemd*'`

- Print output directly to stdout (disable pager):

`systemctl --no-pager list-units`

- Print output without headers or footers (for scripts):

`systemctl --no-legend list-units`
