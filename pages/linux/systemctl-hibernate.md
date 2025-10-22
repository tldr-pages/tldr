# systemctl hibernate

> Hibernate the system by saving the current state to disk and powering off.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#hibernate>.

- Hibernate the system immediately:

`systemctl hibernate`

- Force hibernation even if inhibitors are present:

`systemctl hibernate --force`

- Hibernate the system without sending a message to logged-in users:

`systemctl hibernate --no-wall`
