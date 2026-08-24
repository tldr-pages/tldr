# systemctl-poweroff

> Power off the system.
> See also: `poweroff`.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#poweroff>.

- Power off the system:

`systemctl poweroff`

- Power off the system immediately without asking services to stop gracefully:

`systemctl poweroff {{[-f|--force]}}`

- Power off the system immediately without sending notifications to logged-in users:

`systemctl poweroff {{[-f|--force]}} --no-wall`
