# systemctl is-active

> Check if one or more systemd units are active.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#is-active%20PATTERN%E2%80%A6>.

- Check whether a unit is active:

`systemctl is-active {{unit}}`

- Check whether multiple units are active:

`systemctl is-active {{unit1 unit2 ...}}`

- Check whether a unit is active without printing the state to `stdout`:

`systemctl is-active {{unit}} {{[-q|--quiet]}}`

- Check whether a user unit is active:

`systemctl is-active {{unit}} --user`
