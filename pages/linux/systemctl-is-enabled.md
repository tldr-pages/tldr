# systemctl is-enabled

> Check whether unit files are enabled.
> See also: `systemctl enable`, `systemctl disable`.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#is-enabled%20UNIT%E2%80%A6>.

- Show the enable state:

`systemctl is-enabled {{unit1 unit2 ...}}`

- Suppress output and return only the exit status:

`systemctl is-enabled {{unit}} --quiet`

- Show installation targets and symlink paths:

`systemctl is-enabled {{unit}} --full`
