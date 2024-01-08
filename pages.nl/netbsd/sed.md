# sed

> Pas tekst aan in een op een scriptbare manier.
> Bekijk ook: `awk`, `ed`.
> Meer informatie: <https://man.netbsd.org/sed.1>.

- Vervang alle `apple` (basis regex) met `mango` (basis regex) in alle invoerregels en toon het resultaat in `stdout`::

`{{commando}} | sed 's/apple/mango/g'`

- Voer een specifiek script bestand uit en toon het resultaat in `stdout`:

`{{commando}} | sed -f {{pad/naar/script.sed}}`

- Vertraag het openen van elk bestand tot een commando met de gerelateerde `w`-functie of vlag wordt toegepast op een regel invoer:

`{{commando}} | sed -fa {{pad/naar/script.sed}}`

- Turn on GNU re[g]ex extension:

`{{commando}} | sed -fg {{pad/naar/script.sed}}`

- Vervang alle `apple` (uitgebreide regex) met `APPLE` (uitgebreide regex) in alle invoerregels en toon het resultaat in `stdout`:

`{{commando}} | sed -E 's/(apple)/\U\1/g'`

- Toon alleen de eerste regel in `stdout`:

`{{commando}} | sed -n '1p'`

- Vervang alle `apple` (basis regex) met `mango` (basis regex) in een specifiek bestand en overschrijf het originele bestand:

`sed -i 's/apple/mango/g' {{pad/naar/bestand}}`
