# systemctl help

> Show the manual pages for one or more units, or for the unit a process belongs to (by PID).
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#help%20PATTERN%E2%80%A6%7CPID%E2%80%A6>.

- Show the manual page for a specific unit:

`systemctl help {{unit}}`

- Show the manual pages for multiple units:

`systemctl help {{unit1 unit2 ...}}`

- Show the manual page for a user unit:

`systemctl help {{unit}} --user`

- Show the manual page without a pager (all at once):

`systemctl help {{unit}} --no-pager`

- Show the manual page for the unit of a process by PID:

`systemctl help {{pid}}`
