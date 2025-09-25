# systemctl freeze

> Freeze one or more units.
> Frozen units can be resumed with `systemctl thaw`.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#freeze%20PATTERN%E2%80%A6>.

- Freeze a specific unit:

`systemctl freeze {{unit}}`

- Freeze multiple units:

`systemctl freeze {{unit1 unit2 ...}}`

- Freeze all running units:

`systemctl freeze '*'`
