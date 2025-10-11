# systemctl enable

> Schakel systemd-services aan.
> Meer informatie: <https://www.freedesktop.org/software/systemd/man/systemctl.html#enable%20UNIT%E2%80%A6>.

- Schakel het automatisch opstarten van een service in:

`systemctl enable {{eenheid}}`

- Schakel het automatisch opstarten van een service in en start het nu:

`systemctl enable {{eenheid}} --now`

- Schakel het automatisch opstarten van een gebruikersservice na het inloggen in:

`systemctl enable {{eenheid}} --user`
