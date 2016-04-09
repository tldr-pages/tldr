# systemctl

> Control the systemd system and service manager.

- List failed units:

`systemctl --failed`

- Start/Stop/Restart/Reload a service:

`systemctl start/stop/restart/reload {{unit}}`

- Show the status of a unit:

`systemctl status {{unit}}`

- Enable/Disable a unit to be started on bootup:

`systemctl enable/disable {{unit}}`

- Mask/Unmask a unit, prevent it to be started on bootup:

`systemctl mask/unmask {{unit}}`

- Reload systemd, scanning for new or changed units:

`systemctl daemon-reload`
