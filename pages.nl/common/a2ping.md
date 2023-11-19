# a2ping

> Converteer afbeeldingen in EPS- of PDF-bestanden.
> Meer informatie: <https://manned.org/a2ping>.

- Converteer een afbeelding naar PDF (Opmerking: het opgeven van een uitvoerbestandsnaam is optioneel):

`a2ping {{pad/naar/afbeelding.ext}} {{pad/naar/uitvoer.pdf}}`

- Comprimeer het document met behulp van de opgegeven methode:

`a2ping --nocompress {{none|zip|best|flate}} {{pad/naar/bestand}}`

- Scan HiResBoundingBox indien aanwezig (Opmerking: de standaard is yes):

`a2ping --nohires {{pad/naar/bestand}}`

- Sta pagina-inhoud onder en links van de oorsprong toe (Opmerking: de standaard is no):

`a2ping --below {{pad/naar/bestand}}`

- Geef extra argumenten door aan `gs`:

`a2ping --gsextra {{arguments}} {{pad/naar/bestand}}`

- Geef extra argumenten mee aan het externe programma (bijv. `pdftops`):

`a2ping --extra {{arguments}} {{pad/naar/bestand}}`

- Hulp weergeven:

`a2ping -h`
