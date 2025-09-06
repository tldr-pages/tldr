# df

> Toon een overzicht van het gebruik van het bestandssysteem op het gebied van schijfruimte.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/df-invocation.html>.

- Toon alle bestandssystemen en hun schijfgebruik:

`df`

- Toon alle bestandssystemen en hun schijfgebruik in een leesbaar formaat:

`df {{[-h|--human-readable]}}`

- Toon het bestandssysteem en het schijfgebruik voor het opgegeven bestand of map:

`df {{pad/naar/bestand_of_map}}`

- Neem statistieken op over het aantal beschikbare inodes:

`df {{[-i|--inodes]}}`

- Toon bestandssystemen maar negeer specifieke types:

`df {{[-x|--exclude-type]}} {{squashfs}} {{[-x|--exclude-type]}} {{tmpfs}}`

- Toon bestandssysteem-types:

`df {{[-T|--print-type]}}`
