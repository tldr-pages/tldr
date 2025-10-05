# systemctl list-unit-files

> List installed unit files and their enablement states.
> See also: `systemctl list-units` for listing units currently loaded in memory.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#list-unit-files%20PATTERN%E2%80%A6>.

- List installed unit files and their enablement states:

`systemctl list-unit-files`

- Filter by state (e.g., enabled):

`systemctl list-unit-files --state enabled`

- Filter by a name pattern (e.g., sshd*):

`systemctl list-unit-files 'sshd*'`

- Print output directly to stdout (disable pager):

`systemctl --no-pager list-unit-files`

- Print output without headers or footers (for scripts):

`systemctl --no-legend list-unit-files`
