# xzgrep

> Zoek bestanden die mogelijk worden gecomprimeerd met `xz`, `lzma`, `gzip`, `bzip2`, `lzop`, of `zstd` met behulp van reguliere expressies.
> Zie ook: `grep`.
> Meer informatie: <https://manned.org/xzgrep>.

- Zoek naar een patroon in een bestand:

`xzgrep "{{zoekpatroon}}" {{pad/naar/bestand}}`

- Zoek naar een exacte tekenreeks (schakelt reguliere expressies uit):

`xzgrep --fixed-strings "{{exact_string}}" {{pad/naar/bestand}}`

- Zoek naar een patroon in alle bestanden en geef de regelnummers weer van de overeenkomsten:

`xzgrep --line-number "{{zoekpatroon}}" {{pad/naar/bestand}}`

- Gebruik uitgebreidere reguliere expressies (ondersteund `?`, `+`, `{}`, `()` en `|`), in case-ongevoelige modus:

`xzgrep --extended-regexp --ignore-case "{{zoekpatroon}}" {{pad/naar/bestand}}`

- Toon 3 regels met context rond, voor of na elke overeenkomst:

`xzgrep --{{context|before-context|after-context}}={{3}} "{{zoekpatroon}}" {{pad/naar/bestand}}`

- Toon bestandsnaam en regelnummer voor elke overeenkomst met kleuren:

`xzgrep --with-filename --line-number --color=always "{{zoekpatroon}}" {{pad/naar/bestand}}`

- Zoek naar regels die overeenkomen met een patroon en toon alleen de gematchte tekst:

`xzgrep --only-matching "{{zoekpatroon}}" {{pad/naar/bestand}}`
