# systemctl revert

> Revert unit files to their vendor versions.
> Undoes the effects of `edit`, `enable`, `disable`, `set-property`, and `mask`.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#revert%20UNIT%E2%80%A6>.

- Revert unit files to their default settings:

`systemctl revert {{unit1 unit2 ...}}`

- Revert a user unit file:

`systemctl revert {{unit}} --user`
