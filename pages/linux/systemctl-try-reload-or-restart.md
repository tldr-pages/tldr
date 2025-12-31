# systemctl try-reload-or-restart

> Reload one or more units if they support it; otherwise restart them.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#try-reload-or-restart%20PATTERN%E2%80%A6>.

- Reload or restart a specific unit:

`systemctl try-reload-or-restart {{unit}}`

- Reload or restart multiple units:

`systemctl try-reload-or-restart {{unit1 unit2 ...}}`

- Reload or restart all units matching a pattern:

`systemctl try-reload-or-restart '{{pattern}}'`
