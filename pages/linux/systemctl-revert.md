# systemctl revert

> Revert unit files to their vendor versions.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#revert%20UNIT%E2%80%A6>.

- Revert unit files to their default settings:

`systemctl revert {{unit1 unit2 ...}}`

- Revert a user unit file:

`systemctl revert {{unit}} --user`
