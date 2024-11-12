# date

> Stel de systeemdatum in of toon deze.
> Meer informatie: <https://keith.github.io/xcode-man-pages/date.1.html>.

- Toon de huidige datum in het standaardformaat van de locale:

`date +%c`

- Toon de huidige datum in UTC en ISO 8601-formaat:

`date -u +%Y-%m-%dT%H:%M:%SZ`

- Toon de huidige datum als een Unix timestamp (seconden sinds de Unix-epoch):

`date +%s`

- Toon een specifieke datum (gerepresenteerd als een Unix timestamp) met het standaard formaat:

`date -r {{1473305798}}`
