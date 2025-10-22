# systemctl kill

> Send a signal to one or more processes of a unit.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#kill%20PATTERN%E2%80%A6>.

- Send the `SIGTERM` signal to a unit to terminate it:

`systemctl kill {{unit}}`

- Send a specific signal to a unit:

`systemctl kill {{[-s|--signal]}} {{signal_number|signal_name}} {{unit}}`

- Send a `SIGHUP` signal to only the main process of a unit:

`systemctl kill {{[-s|--signal]}} SIGHUP --kill-whom main {{unit}}`

- List all available signals:

`systemctl kill {{[-s|--signal]}} help`
