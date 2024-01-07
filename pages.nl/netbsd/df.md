# df

> Toon een overzicht van het gebruik van het bestandssysteem op het gebied van schijfruimte.
> Meer informatie: <https://man.netbsd.org/NetBSD-9.3/df.1>.

- Toon alle bestandssystemen en hun schijfgebruik met behulp van 512-byte eenheden:

`df`

- Gebruik leesbare eenheden (gebaseerd op de macht van 1024):

`df -h`

- Toon alle velden van de structu(u)r(en) geretourneerd door `statvfs`:

`df -G`

- Toon het bestandssysteem en het schijfgebruik voor het opgegeven bestand of map:

`df {{pad/naar/bestand_of_map}}`

- Neem statistieken op over het aantal beschikbare en gebruikte [i]-knooppunten:

`df -i`

- Gebruik 1024-byte eenheden voor het schrijven van de ruimte figuren:

`df -k`

- Toon informatie in een [P]ortable wijze:

`df -P`
