# systemctl cat

> Show the full contents of unit files as systemd sees them.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#cat%20PATTERN%E2%80%A6>.

- Show the contents and absolute path of a unit file:

`systemctl cat {{unit}}`

- Show the contents of multiple unit files:

`systemctl cat {{unit1 unit2 ...}}`

- Show the contents of a unit file for a template:

`systemctl cat {{template@}}`

- Show the contents of a user unit file:

`systemctl cat {{unit}} --user`
