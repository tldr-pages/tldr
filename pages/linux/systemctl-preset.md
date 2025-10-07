# systemctl preset

> Reset the enablement state of unit files to the defaults specified in preset policy files.
> See also: `systemctl preset-all`, `systemctl list-unit-files`.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#preset%20UNIT%E2%80%A6>.

- Reset the enablement state to preset defaults:

`systemctl preset {{unit1 unit2 ...}}`

- Control how presets are applied:

`systemctl preset {{unit}} --preset-mode {{full|enable-only|disable-only}}`

- Suppress output and return only the exit code:

`systemctl preset {{unit}} --quiet`
