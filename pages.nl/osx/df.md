# df

> Toon een overzicht van het gebruik van het bestandssysteem op het gebied van schijfruimte.
> Meer informatie: <https://keith.github.io/xcode-man-pages/df.1.html>.

- Toon alle bestandssystemen en hun schijfgebruik met behulp van 512-byte eenheden:

`df`

- Gebruik leesbare eenheden (gebaseerd op de macht van 1024) en toon het grote totaal:

`df -h -c`

- Gebruik leesbare eenheden (gebaseerd op de macht van 1000):

`df -{{-si|H}}`

- Toon het bestandssysteem en het schijfgebruik voor het opgegeven bestand of map:

`df {{pad/naar/bestand_of_map}}`

- Neem statistieken op over het aantal beschikbare en gebruikte [i]-knooppunten inclusief de bestandssysteem t[Y]pes:

`df -iY`

- Gebruik 1024-byte eenheden voor het schrijven van de ruimte figuren:

`df -k`

- Toon informatie in een [P]ortable wijze:

`df -P`
