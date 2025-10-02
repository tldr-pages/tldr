# systemctl daemon-reload

> Reload systemd manager configuration.
> Use this after creating, modifying, or deleting unit files.
> This does **not** reload service configuration; use `systemctl reload` for that.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#daemon-reload>.

- Reload systemd after editing unit files:

`sudo systemctl daemon-reload`

- Reload systemd after creating a new unit:

`sudo systemctl daemon-reload`

- Start a new unit after reloading systemd:

`sudo systemctl start {{myservice}}`

- Reload systemd after modifying a unit:

`sudo systemctl daemon-reload`

- Restart a changed service:

`sudo systemctl restart {{nginx}}`
