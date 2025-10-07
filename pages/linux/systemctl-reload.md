# systemctl reload

> Reload a service's configuration without restarting it.
> This reloads the service itself (like Apache or Nginx configs), not the systemd unit file.
> To reload unit files, use `systemctl daemon-reload`.

- Reload a service:

`systemctl reload {{nginx}}`

- Reload multiple services:

`systemctl reload {{networking apache2 ...}}`

- Reload a service for the current user:

`systemctl reload {{pipewire}} --user`
