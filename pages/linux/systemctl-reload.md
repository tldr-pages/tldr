# systemctl reload

> Reload a service's configuration without restarting it.
> This reloads the service itself (like Apache or `nginx` configs), not the systemd unit file.
> To reload unit files, use `systemctl daemon-reload`.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#reload%20PATTERN%E2%80%A6>

- Reload a service:

`systemctl reload {{nginx}}`

- Reload multiple services:

`systemctl reload {{unit1 unit2 ...}}`

- Reload a service for the current user:

`systemctl reload {{pipewire}} --user`
