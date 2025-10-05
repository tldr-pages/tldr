# systemctl is-active

> Check if one or more systemd units are active.
> Returns either 0 or 1 and prints the state to stdout, unless the `--quiet` flag is specified.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#is-active%20PATTERN%E2%80%A6>.

- Check whether a unit is active:

`systemctl is-active {{unit}}`

- Check whether multiple units are active:

`systemctl is-active {{unit1 unit2 ...}}`

- Check whether a unit is active without printing the state to `stdout`:

`systemctl is-active --quiet {{unit}}`
