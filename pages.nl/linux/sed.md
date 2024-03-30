# sed

> Pas tekst aan in een op een scriptbare manier.
> Bekijk ook: `awk`, `ed`.
> Meer informatie: <https://www.gnu.org/software/sed/manual/sed.html>.

- Vervang alle `apple` (basis regex) met `mango` (basis regex) in alle invoerregels en toon het resultaat in `stdout`:

`{{commando}} | sed 's/apple/mango/g'`

- Vervang alle `apple` (uitgebreide regex) met `APPLE` (uitgebreide regex) in alle invoerregels en toon het resultaat in `stdout`:

`{{commando}} | sed -E 's/(apple)/\U\1/g'`

- Vervang alle `apple` (basis regex) met `mango` (basis regex) in een specifiek bestand en overschrijf het originele bestand:

`sed -i 's/apple/mango/g' {{pad/naar/bestand}}`

- Voer een specifiek script bestand uit en toon het resultaat in `stdout`:

`{{commando}} | sed -f {{pad/naar/script.sed}}`

- Toon alleen de eerste regel in `stdout`:

`{{commando}} | sed -n '1p'`

- Verwijder de eerste regel van een bestand:

`sed -i 1d {{pad/naar/bestand}}`

- Voeg een nieuwe regel in bij de eerste regel van een bestand:

`sed -i '1i\your new line text\' {{pad/naar/bestand}}`
