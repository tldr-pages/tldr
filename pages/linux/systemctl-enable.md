# systemctl enable

> Enable Systemd services.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#enable%20UNIT%E2%80%A6>.

- Enable a service to run on boot:

`systemctl enable {{unit}}`

- Enable a service to run on boot and start it now:

`systemctl enable {{unit}} --now`
