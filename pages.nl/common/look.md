# look

> Toon regels die beginnen met een prefix in een gesorteerd bestand.
> Let op: de regels in het bestand moeten gesorteerd zijn.
> Zie ook: `grep`, `sort`.
> Meer informatie: <https://man.openbsd.org/look>.

- Zoek naar regels die beginnen met een specifieke prefix in een specifiek bestand:

`look {{prefix}} {{pad/naar/bestand}}`

- Zoek hoofdletterongevoelig alleen op alfanumerieke tekens:

`look {{[-f|--ignore-case]}} {{[-d|--alphanum]}} {{prefix}} {{pad/naar/bestand}}`

- Specificeer een karakter voor het beëindigen van een string (standaard een spatie):

`look {{[-t|--terminate]}} {{,}}`

- Zoek in `/usr/share/dict/words` (`--alphanum` en `--ignore-case` worden verondersteld):

`look {{prefix}}`
