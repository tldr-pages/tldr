# sed

> Pas tekst aan in een op een scriptbare manier.
> Zie ook: `awk`, `ed`.
> Meer informatie: <https://www.gnu.org/software/sed/manual/sed.html>.

- Vervang alle `apple` (basis regex) met `mango` (basis regex) in alle invoerregels en toon het resultaat in `stdout`:

`{{commando}} | sed 's/apple/mango/g'`

- Vervang alle `apple` (uitgebreide regex) met `APPLE` (uitgebreide regex) in alle invoerregels en toon het resultaat in `stdout`:

`{{commando}} | sed {{[-E|--regexp-extended]}} 's/(apple)/\U\1/g'`

- Gebruik basisregex om `apple` te vervangen door `mango` en `orange` door `lime` in een bestand (waarbij het originele bestand wordt overschreven):

`sed {{[-i|--in-place]}} -e 's/apple/mango/g' -e 's/orange/lime/g' {{pad/naar/bestand}}`

- Voer een specifiek script bestand uit en toon het resultaat in `stdout`:

`{{commando}} | sed {{-f|--file}} {{pad/naar/script.sed}}`

- Toon alleen de eerste regel in `stdout`:

`{{commando}} | sed {{[-n|--quiet]}} '1p'`

- Verwij[d]er regels 1 tot en met 5 van een bestand en maak een back-up van het originele bestand met een `.orig` extensie:

`sed {{[-i|--in-place=]}}{{.orig}} '1,5d' {{pad/naar/bestand}}`

- Voeg een nieuwe regel in bij de eerste regel van een bestand:

`sed {{[-i|--in-place]}} '1i\your new line text\' {{pad/naar/bestand}}`

- Verwijder lege regels (met of zonder spaties/tabtekens) uit een bestand, waarbij het oorspronkelijke bestand ter plaatse wordt overschreven:

`sed {{[-i|--in-place]}} '/^[[:space:]]*$/d' {{pad/naar/bestand}}`
