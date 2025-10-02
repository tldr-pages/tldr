# systemctl daemon-reload

> Reload systemd manager configuration.
> Use this after creating, modifying, or deleting unit files.
> This does not reload service configuration; use `systemctl reload` for that.

- Reload systemd after editing unit files:

`systemctl daemon-reload`

- Reload systemd after creating a new unit:

`systemctl daemon-reload`

- Start a new unit after reloading systemd:

`systemctl start {{myservice}}`

- Reload systemd after modifying a unit:

`systemctl daemon-reload`

- Restart a changed service:

`systemctl restart {{nginx}}`
