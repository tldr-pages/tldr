# svcs

> Geef informatie over actieve services.
> Meer informatie: <https://www.unix.com/man-page/sunos/1/svcs>.

- Toon alle actieve services:

`svcs`

- Toon inactieve services:

`svcs -vx`

- Geef informatie over een specifieke service:

`svcs apache`

- Toon de locatie van het logbestand van een service:

`svcs -L apache`

- Toon de laatste lijnen van het logbestand van een service:

`tail $(svcs -L apache)`
