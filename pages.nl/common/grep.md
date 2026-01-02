# grep

> Zoek patronen in bestanden met behulp van `regex`en.
> Zie ook: `regex`.
> Meer informatie: <https://www.gnu.org/software/grep/manual/grep.html>.

- Zoek naar een patroon in bestanden:

`grep "{{zoekpatroon}}" {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Zoek naar een exacte string (schakelt `regex` uit):

`grep {{[-F|--fixed-strings]}} "{{exacte_string}}" {{pad/naar/bestand}}`

- Zoek naar een patroon in alle bestanden in een map recursief, waarbij binaire bestanden genegeerd worden:

`grep {{[-rI|--recursive --binary-files=without-match]}} "{{zoekpatroon}}" {{pad/naar/map}}`

- Toon 3 regels met [C]ontext rond, voor ([B]) of n[A] elke overeenkomst:

`grep {{--context|--before-context|--after-context}} 3 "{{zoekpatroon}}" {{pad/naar/bestand}}`

- Print bestandsnaam en regelnummers voor elke overeenkomst met kleuruitvoer:

`grep {{[-Hn|--with-filename --line-number]}} --color=always "{{zoekpatroon}}" {{pad/naar/bestand}}`

- Toon alleen de overeenkomende tekst:

`grep {{[-o|--only-matching]}} "{{zoekpatroon}}" {{pad/naar/bestand}}`

- Lees data vanuit `stdin` en toon niet de regels die overeenkomen met een patroon:

`cat {{pad/naar/bestand}} | grep {{[-v|--invert-match]}} "{{zoekpatroon}}"`

- Gebruik uitgebreide `regex`en (ondersteunt `?`, `+`, `{}`, `()` en `|`), in hoofdletterongevoelige modus:

`grep {{[-Ei|--extended-regexp --ignore-case]}} "{{zoekpatroon}}" {{pad/naar/bestand}}`
