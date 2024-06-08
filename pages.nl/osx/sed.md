# sed

> Pas tekst aan in een op een scriptbare manier.
> Bekijk ook: `awk`, `ed`.
> Meer informatie: <https://keith.github.io/xcode-man-pages/sed.1.html>.

- Vervang alle `apple` (basis regex) met `mango` (basis regex) in alle invoerregels en toon het resultaat in `stdout`:

`{{commando}} | sed 's/apple/mango/g'`

- Voer een specifiek script bestand uit en toon het resultaat in `stdout`:

`{{commando}} | sed -f {{pad/naar/script_bestand.sed}}`

- Vervang alle `apple` (uitgebreide regex) met `APPLE` (uitgebreide regex) in alle invoerregels en toon het resultaat in `stdout`:

`{{commando}} | sed -E 's/(apple)/\U\1/g'`

- Toon alleen de eerste regel in `stdout`:

`{{commando}} | sed -n '1p'`

- Vervang alle `apple` (basis regex) met `mango` (basis regex) in een specifiek `bestand` en sla een backup op van het origineel in `bestand.bak`:

`sed -i bak 's/apple/mango/g' {{pad/naar/bestand}}`
