# df

> Toon een overzicht van het gebruik van het bestandssysteem op het gebied van schijfruimte.
> Meer informatie: <https://man.freebsd.org/cgi/man.cgi?query=df>.

- Toon alle bestandssystemen en hun schijfgebruik met behulp van 512-byte eenheden:

`df`

- Gebruik leesbare eenheden (gebaseerd op de macht van 1024) en toon het grote totaal:

`df -h -c`

- Gebruik leesbare eenheden (gebaseerd op de macht van 1000):

`df -{{-si|H}}`

- Toon het bestandssysteem dat het opgegeven bestand of de map bevat:

`df {{pad/naar/bestand_of_map}}`

- Neem statistieken op over het aantal beschikbare en gebruikte [i]-knooppunten inclusief de bestandssysteem [T]ypes:

`df -iT`

- Gebruik [k]ibibyte-eenheden (1024 byte) voor het weergeven van de groottecijfers:

`df -k`

- Toon informatie op een [P]ortable wijze:

`df -P`
