# systemctl hybrid-sleep

> Put the system into hybrid sleep, which combines suspend-to-RAM and hibernate.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#hybrid-sleep>.

- Put the system into hybrid sleep immediately:

`systemctl hybrid-sleep`

- Force hybrid sleep even if inhibitors are present:

`systemctl hybrid-sleep --force`

- Put the system into hybrid sleep without sending a wall message to logged-in users:

`systemctl hybrid-sleep --no-wall`
