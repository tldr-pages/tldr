# systemctl stop

> Stop systemd eenheden.
> Meer informatie: <https://www.freedesktop.org/software/systemd/man/systemctl.html#stop%20PATTERN%E2%80%A6>.

- Stop een eenheid:

`systemctl stop {{eenheid}}`

- Stop een service en onderdruk waarschuwingen:

`systemctl stop {{eenheid}} --no-warn`

- Stop een gebruikerseenheid:

`systemctl stop {{eenheid}} --user`
