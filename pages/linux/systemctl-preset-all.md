# systemctl preset-all

> Reset the enablement state of all installed units to the defaults specified in preset policy files.
> See also: `systemctl preset`, `systemctl list-unit-files`.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#preset-all>.

- Reset the enablement state of all installed units:

`sudo systemctl preset-all`

- Enable only if marked as enabled in the preset policy:

`sudo systemctl preset-all --preset-mode enable-only`

- Disable only if marked as disabled in the preset policy:

`sudo systemctl preset-all --preset-mode disable-only`

- Suppress output and return only the exit code:

`sudo systemctl preset-all {{[-q|--quiet]}}`
