# systemctl disable

> Disable systemd services.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#disable%20UNIT%E2%80%A6>.

- Stop a service from running on boot:

`sudo systemctl disable {{unit}}`

- Stop a service from running on boot and stop its current execution:

`sudo systemctl disable {{unit}} --now`

- Stop a user service from running on login:

`sudo systemctl disable {{unit}} --user`
