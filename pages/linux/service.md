# service

> Manage services by running init scripts.
> The full script path should be omitted (/etc/init.d/ is assumed).

- Start/Stop/Restart/Reload service (start/stop should always be available):

`service {{init_script}} {{start|stop|restart|reload}}`

- Do a full restart (runs script twice with start and stop):

`service {{init_script}} --full-restart`

- Show the current status of a service:

`service {{init_script}} status`

- List the status of all services:

`service --status-all`
