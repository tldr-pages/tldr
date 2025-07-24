# systemctl enable

> Schakel systemd-services aan.
> Meer informatie: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#enable%20UNIT%E2%80%A6>.

- Schakel het automatisch opstarten van een service aan:

`systemctl enable {{eenheid}}`

- Schakel het automatisch opstarten van een service aan en start het nu:

`systemctl enable {{eenheid}} --now`
