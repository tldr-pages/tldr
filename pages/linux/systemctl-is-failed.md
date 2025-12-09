# systemctl is-failed

> Check if one or more systemd units have failed.
> See also: `systemctl is-active`, `systemctl status`.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#is-failed%20PATTERN%E2%80%A6>.

- Check if there are any failed units:

`systemctl is-failed`

- Check if a unit or multiple units have failed:

`systemctl is-failed {{unit1 unit2 ...}}`

- Suppress output and return only the exit code:

`systemctl is-failed {{unit}} {{[-q|--quiet]}}`

- Check if a user unit has failed:

`systemctl is-failed {{unit}} --user`
