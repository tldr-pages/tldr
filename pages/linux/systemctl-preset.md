# systemctl preset

> Reset the enablement state of unit files to the defaults specified in preset policy files.
> See also: `systemctl preset-all`, `systemctl list-unit-files`.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#preset%20UNIT%E2%80%A6>.

- Reset the enablement state to preset defaults:

`systemctl preset {{unit1 unit2 ...}}`

- Enable only if marked as enabled in the preset policy:

`systemctl preset {{unit}} --preset-mode enable-only`

- Disable only if marked as disabled in the preset policy:

`systemctl preset {{unit}} --preset-mode disable-only`

- Suppress output and return only the exit code:

`systemctl preset {{unit}} {{[-q|--quiet]}}`
