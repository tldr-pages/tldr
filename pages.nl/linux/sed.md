# sed

> GNU stream-editor voor het filteren en transformeren van tekst.
> Zie ook: `awk`, `ed`.
> Meer informatie: <https://www.gnu.org/software/sed/manual/sed.html>.

- Vervang ([s]) alle voorkomens van "apple" door "mango" in alle regels en toon het resultaat naar `stdout`:

`{{commando}} | sed 's/apple/mango/g'`

- Vervang alle "apple" met "mango" in een bestand (waarbij het originele bestand wordt overschreven):

`sed {{[-i|--in-place]}} 's/apple/mango/g' {{pad/naar/bestand}}`

- Voer meerdere vervangingen uit in één commando:

`{{commando}} | sed -e '{{s/appel/mango/g}}' -e '{{s/sinaasappel/limoen/g}}'`

- Gebruik een aangepast scheidingsteken (handig als het patroon `/` bevat):

`{{commando}} | sed '{{s#////#____#g}}'`

- Verwij[d]er regels 1 tot en met 5 van een bestand en maak een back-up van het originele bestand met een `.orig` extensie:

`sed {{[-i|--in-place=]}}.orig '1,5d' {{pad/naar/bestand}}`

- Toon ([p]) alleen de eerste regel naar `stdout`:

`{{commando}} | sed {{[-n|--quiet]}} '1p'`

- Voeg ([i]) een nieuwe regel in aan het begin van een bestand, waarbij het originele bestand wordt overschreven:

`sed {{[-i|--in-place]}} '1i\your new line text\' {{pad/naar/bestand}}`

- Verwijder lege regels (met of zonder spaties/tabtekens) uit een bestand, waarbij het oorspronkelijke bestand wordt overschreven:

`sed {{[-i|--in-place]}} '/^[[:space:]]*$/d' {{pad/naar/bestand}}`
