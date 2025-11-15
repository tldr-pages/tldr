# systemctl restart

> Stop and then start one or more systemd units.
> Can be used in place of `systemctl start` on a stopped unit, but `start` is safer so that a running unit isn't accidentally restarted.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#restart%20PATTERN%E2%80%A6>.

- Restart a unit:

`systemctl restart {{unit}}`

- Restart more than one unit:

`systemctl restart {{unit1 unit2 ...}}`

- Restart a user unit:

`systemctl restart {{unit}} --user`
