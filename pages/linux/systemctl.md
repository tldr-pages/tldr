# systemctl

> Control the systemd system and service manager.

- List failed units:

`systemctl --failed`

- Start/Stop/Restart a service:

`systemctl start/stop/restart {{unit}}`

- Show the status of a unit:

`systemctl status {{unit}}`

- Enable/Disable a unit to be started on bootup:

`systemctl enable/disable {{unit}}`

- Reload systemd, scanning for new or changed units:

`systemctl daemon-reload`
