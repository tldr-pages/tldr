# systemctl try-reload-or-restart

> Herlaad een of meer eenheden als ze dit ondersteunen; start ze anders opnieuw op.
> Meer informatie: <https://www.freedesktop.org/software/systemd/man/systemctl.html#try-reload-or-restart%20PATTERN%E2%80%A6>.

- Herlaad of herstart een specifieke eenheid:

`systemctl try-reload-or-restart {{eenheid}}`

- Herlaad of herstart meerdere eenheden:

`systemctl try-reload-or-restart {{eenheid1 eenheid2 ...}}`

- Herlaad of herstart alle eenheden die overeenkomen met een patroon:

`systemctl try-reload-or-restart '{{patroon}}'`
