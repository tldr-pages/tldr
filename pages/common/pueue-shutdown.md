# pueue shutdown

> Remotely shut down the daemon.
> only use this subcommand if the daemon isn't started by a service manager

- shutdown the daemon without a service manager

`pueue shutdown`

- shutdown the daemon with systemd

`systemctl --user disable --now pueued.service`
