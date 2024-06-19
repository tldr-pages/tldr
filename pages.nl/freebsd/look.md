# look

> Toon regels die beginnen met een prefix in een gesorteerd bestand.
> Bekijk ook: `grep`, `sort`.
> Meer informatie: <https://man.freebsd.org/cgi/man.cgi?look>.

- Zoek naar regels die beginnen met een specifieke prefix in een specifiek bestand:

`look {{prefix}} {{pad/naar/bestand}}`

- Zoek hoofdletterongevoelig alleen op alfanumerieke tekens:

`look {{-f|--ignore-case}} {{-d|--alphanum}} {{prefix}} {{pad/naar/bestand}}`

- Specificeer een string-terminatiekarakter (standaard is spatie):

`look {{-t|--terminate}} {{,}}`

- Zoek in `/usr/share/dict/words` (`--ignore-case` en `--alphanum` worden aangenomen):

`look {{prefix}}`
