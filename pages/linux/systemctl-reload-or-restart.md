# systemctl reload-or-restart

> Reload `systemd` unit(s) otherwise restart them.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#reload-or-restart%20PATTERN%E2%80%A6>.

- Reload or restart a unit:

`systemctl reload-or-restart {{unit}}`

- Reload or restart multiple units matching a pattern:

`systemctl reload-or-restart {{pattern}}`

- Run the command without waiting for the operation to complete:

`systemctl reload-or-restart {{unit}} --no-block`

- Apply the command only to user units:

`systemctl reload-or-restart {{unit}} --user`
