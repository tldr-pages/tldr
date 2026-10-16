# systemctl revert

> Zet eenheidsbestanden terug naar hun leveranciersversies.
> Maakt de effecten van `edit`, `enable`, `disable`, `set-property` en `mask` ongedaan.
> Meer informatie: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#revert%20UNIT%E2%80%A6>.

- Zet eenheidsbestanden terug naar hun standaardinstellingen:

`systemctl revert {{eenheid1 eenheid2 ...}}`

- Zet een gebruikerseenheidsbestand terug:

`systemctl revert {{eenheid}} --user`
