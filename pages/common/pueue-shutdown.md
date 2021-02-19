# pueue shutdown

> Remotely shut down the daemon.
> Only use this subcommand if the daemon isn't started by a service manager.

- Shutdown the daemon without a service manager:

`pueue shutdown`

- Shutdown the daemon with systemd:

`systemctl --user disable --now pueued.service`
