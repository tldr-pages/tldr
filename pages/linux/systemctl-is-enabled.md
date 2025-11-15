# systemctl is-enabled

> Check whether unit files are enabled.
> See also: `systemctl enable`, `systemctl disable`.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#is-enabled%20UNIT%E2%80%A6>.

- Show the enablement state:

`systemctl is-enabled {{unit1 unit2 ...}}`

- Suppress output and return only the exit code:

`systemctl is-enabled {{unit}} --quiet`

- Show installation targets and symlink paths:

`systemctl is-enabled {{unit}} --full`
