# systemctl disable

> Disable systemd services.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#disable%20UNIT%E2%80%A6>.

- Stop a service from running on boot:

`systemctl disable {{unit}}`

- Stop a service from running on boot and stop its current execution:

`systemctl disable {{unit}} --now`
