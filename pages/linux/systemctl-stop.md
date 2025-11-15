# systemctl stop

> Stop systemd units.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#stop%20PATTERN%E2%80%A6>.

- Stop a unit:

`systemctl stop {{unit}}`

- Stop a service and suppress warnings:

`systemctl stop {{unit}} --no-warn`

- Stop a user unit:

`systemctl stop {{unit}} --user`
