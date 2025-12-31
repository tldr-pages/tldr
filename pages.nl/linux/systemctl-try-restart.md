# systemctl try-restart

> Herstart een of meer eenheden als ze momenteel actief zijn.
> Meer informatie: <https://www.freedesktop.org/software/systemd/man/systemctl.html#try-restart%20PATTERN%E2%80%A6>.

- Start een specifieke eenheid opnieuw als deze draait:

`systemctl try-restart {{eenheid}}`

- Herstart meerdere eenheden als ze draaien:

`systemctl try-restart {{eenheid1 eenheid2 ...}}`

- Herstart alle eenheden die overeenkomen met een patroon, als ze actief zijn:

`systemctl try-restart '{{patroon}}'`
