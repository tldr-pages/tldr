# systemctl suspend-then-hibernate

> Suspend the system, then automatically hibernate after a period of inactivity.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#suspend-then-hibernate>.

- Suspend the system and hibernate after the configured delay:

`systemctl suspend-then-hibernate`

- Force suspend-then-hibernate (bypass inhibitor locks):

`systemctl suspend-then-hibernate --force`
