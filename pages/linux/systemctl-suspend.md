# systemctl suspend

> Suspend the system.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#suspend>.

- Suspend the system immediately:

`systemctl suspend`

- Schedule a suspend after a 5 minute delay:

`sleep 300 && systemctl suspend`

- Suspend the system and then hibernate after a delay:

`systemctl hybrid-sleep`
