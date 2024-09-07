# look

> Toon regels die beginnen met een prefix in een gesorteerd bestand.
> Let op: de regels in het bestand moeten gesorteerd zijn.
> Bekijk ook: `grep`, `sort`.
> Meer informatie: <https://manned.org/look>.

- Zoek naar regels die beginnen met een specifieke prefix in een specifiek bestand:

`look {{prefix}} {{pad/naar/bestand}}`

- Zoek hoofdletterongevoeling alleen op lege en alfanumerieke tekens:

`look {{-f|--ignore-case}} {{-d|--alphanum}} {{prefix}} {{pad/naar/bestand}}`

- Specificeer een string-terminatiekarakter (standaard is spatie):

`look {{-t|--terminate}} {{,}}`

- Zoek in `/usr/share/dict/words` (`--ignore-case` en `--alphanum` worden aangenomen):

`look {{prefix}}`

- Zoek in `/usr/share/dict/web2` (`--ignore-case` en `--alphanum` worden aangenomen):

`look {{-a|--alternative}} {{prefix}}`
