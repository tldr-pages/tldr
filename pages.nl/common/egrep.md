# egrep

> Vind patronen in bestanden door gebruik te maken van uitgebreidere reguliere expressies (ondersteund `?`, `+`, `{}`, `()` en `|`).
> Meer informatie: <https://manned.org/egrep>.

- Zoek naar een patroon in een bestand:

`egrep "{{zoekpatroon}}" {{pad/naar/bestand}}`

- Zoek naar een patroon in meerdere bestanden:

`egrep "{{zoekpatroon}}" {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Zoek in `stdin` naar een patroon:

`cat {{pad/naar/bestand}} | egrep {{zoekpatroon}}`

- Toon de bestandsnaam en het regelnummer voor iedere overeenkomst:

`egrep --with-filename --line-number "{{zoekpatroon}}" {{pad/naar/bestand}}`

- Zoek recursief in alle bestanden in een map voor een patroon, maar negeer binaire bestanden:

`egrep --recursive --binary-files={{without-match}} "{{zoekpatroon}}" {{pad/naar/map}}`

- Zoek voor regels die niet voldoen aan een patroon:

`egrep --invert-match "{{zoekpatroon}}" {{pad/naar/bestand}}`
