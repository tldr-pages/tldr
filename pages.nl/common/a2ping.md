# a2ping

> Converteer afbeeldingen in EPS- of PDF-bestanden.
> Meer informatie: <https://manned.org/a2ping>.

- Converteer een afbeelding naar PDF (Let op: het opgeven van een uitvoerbestandsnaam is optioneel):

`a2ping {{pad/naar/afbeelding.ext}} {{pad/naar/uitvoer.pdf}}`

- Comprimeer het document met behulp van de opgegeven methode:

`a2ping --nocompress {{none|zip|best|flate}} {{pad/naar/bestand}}`

- Scan HiResBoundingBox indien aanwezig (Let op: de standaard is ja):

`a2ping --nohires {{pad/naar/bestand}}`

- Sta pagina-inhoud onder en links van de oorsprong toe (Let op: de standaard is nee):

`a2ping --below {{pad/naar/bestand}}`

- Geef extra argumenten door aan `gs`:

`a2ping --gsextra {{argumenten}} {{pad/naar/bestand}}`

- Geef extra argumenten mee aan het externe programma (bijv. `pdftops`):

`a2ping --extra {{argumenten}} {{pad/naar/bestand}}`

- Toon de help:

`a2ping {{[-h|--help]}}`
