# xzgrep

> Zoek bestanden die mogelijk worden gecomprimeerd met `xz`, `lzma`, `gzip`, `bzip2`, `lzop`, of `zstd` met behulp van reguliere expressies.
> Zie ook: `grep`.
> Meer informatie: <https://manned.org/xzgrep>.

- Zoek naar een patroon in een bestand:

`xzgrep "{{zoekpatroon}}" {{pad/naar/bestand}}`

- Zoek naar een exacte tekenreeks (schakelt reguliere expressies uit):

`xzgrep {{[-F|--fixed-strings]}} "{{exacte_string}}" {{pad/naar/bestand}}`

- Zoek naar een patroon in alle bestanden en geef de regelnummers weer van de overeenkomsten:

`xzgrep {{[-n|--line-number]}} "{{zoekpatroon}}" {{pad/naar/bestand}}`

- Toon 3 regels rondom [C]ontext, voor ([B]) of na ([A]) elke overeenkomst:

`xzgrep {{--context|--before-context|--after-context}} 3 "{{zoekpatroon}}" {{pad/naar/bestand}}`

- Toon bestandsnaam en regelnummer voor elke overeenkomst met kleuren:

`xzgrep {{[-H|--with-filename]}} {{[-n|--line-number]}} --color=always "{{zoekpatroon}}" {{pad/naar/bestand}}`

- Zoek naar regels die overeenkomen met een patroon en toon alleen de gematchte tekst:

`xzgrep {{[-o|--only-matching]}} "{{zoekpatroon}}" {{pad/naar/bestand}}`

- Gebruik uitgebreide `regex` (ondersteunt `?`, `+`, `{}`, `()` en `|`), in hoofdletterongevoelige modus:

`xzgrep {{[-E|--extended-regexp]}} {{[-i|--ignore-case]}} "{{zoekpatroon}}" {{pad/naar/bestand}}`
