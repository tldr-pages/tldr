# grep

> Zoek patronen in bestanden met behulp van reguliere expressies.
> Meer informatie: <https://www.gnu.org/software/grep/manual/grep.html>.

- Zoek naar een patroon in een bestand:

`grep "{{zoekpatroon}}" {{pad/naar/bestand}}`

- Zoek naar een exacte string (schakelt reguliere expressies uit):

`grep {{[-F|--fixed-strings]}} "{{exacte_string}}" {{pad/naar/bestand}}`

- Zoek naar een patroon in alle bestanden in een map, recursief, toon regelnummers van overeenkomsten, negeer binaire bestanden:

`grep {{[-rnI|--recursive --line-number --binary-files=without-match]}} "{{zoekpatroon}}" {{pad/naar/map}}`

- Gebruik uitgebreide reguliere expressies (ondersteunt `?`, `+`, `{}`, `()` en `|`), in hoofdletterongevoelige modus:

`grep {{[-Ei|--extended-regexp --ignore-case]}} "{{zoekpatroon}}" {{pad/naar/bestand}}`

- Print 3 regels context rondom, voor of na elke overeenkomst:

`grep {{--context|--before-context|--after-context}} 3 "{{zoekpatroon}}" {{pad/naar/bestand}}`

- Print bestandsnaam en regelnummers voor elke overeenkomst met kleuruitvoer:

`grep {{[-Hn|--with-filename --line-number]}} --color=always "{{zoekpatroon}}" {{pad/naar/bestand}}`

- Zoek naar regels die overeenkomen met een patroon en print alleen de overeenkomstige tekst:

`grep {{[-o|--only-matching]}} "{{zoekpatroon}}" {{pad/naar/bestand}}`

- Zoek in `stdin` naar regels die niet overeenkomen met een patroon:

`cat {{pad/naar/bestand}} | grep {{[-v|--invert-match]}} "{{zoekpatroon}}"`
