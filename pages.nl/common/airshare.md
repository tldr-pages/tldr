# airshare

> Gegevens overdragen tussen twee machines in een lokaal netwerk.
> Meer informatie: <https://airshare.rtfd.io/en/latest/cli.html>.

- Bestanden of mappen delen:

`airshare {{code}} {{pad/naar/bestand_of_map1 pad/naar/bestand_of_map2 ...}}`

- Ontvang een bestand:

`airshare {{code}}`

- Host een ontvangende server (gebruik deze om bestanden te kunnen uploaden via de webinterface):

`airshare --upload {{code}}`

- Stuur bestanden of mappen naar een ontvangende server:

`airshare --upload {{code}} {{pad/naar/bestand_of_map1 pad/naar/bestand_of_map2 ...}}`

- Bestanden verzenden waarvan de paden naar het klembord zijn gekopieerd:

`airshare --file-path {{code}}`

- Ontvang een bestand en kopieer het naar het klembord:

`airshare --clip-receive {{code}}`
