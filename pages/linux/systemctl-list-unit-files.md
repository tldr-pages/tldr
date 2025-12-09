# systemctl list-unit-files

> List installed unit files and their enablement states.
> See also: `systemctl list-units` for listing units currently loaded in memory.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#list-unit-files%20PATTERN%E2%80%A6>.

- List installed unit files and their states:

`systemctl list-unit-files`

- Filter by state:

`systemctl list-unit-files --state {{enabled|disabled|static|...}}`

- Filter by unit type:

`systemctl list-unit-files {{[-t|--type]}} {{service|socket|timer|...}}`

- Filter by a name pattern:

`systemctl list-unit-files '{{sshd*}}'`

- Print output directly to `stdout`:

`systemctl list-unit-files --no-pager`

- Print output without headers or footers:

`systemctl list-unit-files --no-legend`
