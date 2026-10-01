# cupsd

> Server daemon voor de CUPS print server.
> Meer informatie: <https://openprinting.github.io/cups/doc/man-cupsd.html>.

- Start `cupsd` op de achtergrond, aka. als een daemon:

`cupsd`

- Start `cupsd` op de voorgrond:

`cupsd -f`

- Draai `cupsd` op aanvraag (vaak gebruikt door `launchd` of `systemd`):

`cupsd -l`

- Start `cupsd` met het gespecificeerde `cupsd.conf` [c]onfiguratiebestand:

`cupsd -c {{pad/naar/cupsd.conf}}`

- Start `cupsd` met het gespecificeerde `cups-files.conf` configuratiebestand:

`cupsd -s {{pad/naar/cups-files.conf}}`

- [t]est het `cupsd.conf` [c]onfiguratiebestand voor fouten:

`cupsd -t -c {{pad/naar/cupsd.conf}}`

- [t]est het `cups-files.conf` configuratiebestand voor fouten:

`cupsd -t -s {{pad/naar/cups-files.conf}}`

- Toon de help:

`cupsd -h`
