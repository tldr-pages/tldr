# svcs

> Geef informatie over actieve services.
> Meer informatie: <https://www.unix.com/man-page/linux/1/svcs>.

- Oplijsting van alle actieve services:

`svcs`

- Oplijsting van alle inactieve services:

`svcs -vx`

- Geef informatie over een specifieke service:

`svcs apache`

- Toon de locatie van de log file van een service:

`svcs -L apache`

- Toon de laatste lijnen van een service log file:

`tail $(svcs -L apache)`
