# systemctl revert

> Zet unit-bestanden terug naar hun leveranciersversies.
> Maakt de effecten van `edit`, `enable`, `disable`, `set-property` en `mask` ongedaan.
> Meer informatie: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#revert%20UNIT%E2%80%A6>.

- Zet unit-bestanden terug naar hun standaardinstellingen:

`systemctl revert {{eenheid1 eenheid2 ...}}`

- Zet een gebruikers-unit-bestand terug:

`systemctl revert {{eenheid}} --user`
