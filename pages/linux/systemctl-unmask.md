# systemctl unmask

> Unmask units to make them startable again.
> This undoes the effect of `systemctl mask`.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#unmask%20UNIT%E2%80%A6>.

- Unmask a service:

`systemctl unmask {{service_name}}`

- Unmask and start a service immediately:

`systemctl unmask {{service_name}} --now`

- Unmask a user service:

`systemctl unmask {{service_name}} --user`
