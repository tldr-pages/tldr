# systemctl

> Control the systemd system and service manager.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html>.

- Show all running services:

`systemctl status`

- List failed units:

`systemctl --failed`

- Start/Stop/Restart/Reload/Show the status a service:

`systemctl {{start|stop|restart|reload|status}} {{unit}}`

- Enable/Disable a unit to be started on bootup:

`systemctl {{enable|disable}} {{unit}}`

- Reload systemd, scan for new or changed units:

`systemctl daemon-reload`

- Check if a unit is active/enabled/failed:

`systemctl {{is-active|is-enabled|is-failed}} {{unit}}`

- List all service/socket/automount units filtering by running/failed state:

`systemctl list-units --type={{service|socket|automount}} --state={{failed|running}}`

- Show the contents & absolute path of a unit file:

`systemctl cat {{unit}}`
