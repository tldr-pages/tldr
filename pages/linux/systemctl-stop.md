# systemctl stop

> Stop systemd units.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#stop%20PATTERN%E2%80%A6>.

- Stop a unit:

`systemctl stop {{unit}}`

- Stop a service and suppress warnings:

`systemctl stop --no-warn {{unit}}`

- Stop a user unit:

`systemctl stop --user {{unit}}`
