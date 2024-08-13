# look

> Toon regels die beginnen met een prefix in een gesorteerd bestand.
> Let op: de regels in het bestand moeten gesorteerd zijn.
> Bekijk ook: `grep`, `sort`.
> Meer informatie: <https://man.openbsd.org/look>.

- Zoek naar regels die beginnen met een specifieke prefix in een specifiek bestand:

`look {{prefix}} {{pad/naar/bestand}}`

- Zoek hoofdletterongevoelig ([f]) alleen op alfanumerieke tekens ([d]):

`look -f -d {{prefix}} {{pad/naar/bestand}}`

- Specificeer een string-[t]erminatiekarakter (standaard is spatie):

`look -t {{,}}`

- Zoek in `/usr/share/dict/words` (`--ignore-case` en `--alphanum` worden aangenomen):

`look {{prefix}}`
