# cupsd

> Server daemon voor de CUPS print server.
> Meer informatie: <https://openprinting.github.io/cups/doc/man-cupsd.html>.

- Start `cupsd` op de achterground, aka. als een daemon:

`cupsd`

- Start `cupsd` op de voorgrond:

`cupsd -f`

- Draai `cupsd` op aanvraag (vaak gebruikt door `launchd` of `systemd`):

`cupsd -l`

- Start `cupsd` met het gespecificeerde [`c`]`upsd.conf` configuratie bestand:

`cupsd -c {{pad/naar/cupsd.conf}}`

- Start `cupsd` met het gespecificeerde `cups-bestanden.conf` configuratie bestand:

`cupsd -s {{pad/naar/cups-bestanden.conf}}`

- [t]est het [`c`]`upsd.conf` configuratie bestand voor fouten:

`cupsd -t -c {{pad/naar/cupsd.conf}}`

- [t]est het `cups-bestanden.conf` configuratie bestand voor fouten:

`cupsd -t -s {{pad/naar/cups-bestanden.conf}}`

- Toon alle beschikbare opties:

`cupsd -h`
