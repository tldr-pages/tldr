# df

> Toon een overzicht van het gebruik van het bestandssysteem op het gebied van schijfruimte.
> Meer informatie: <https://www.gnu.org/software/coreutils/df>.

- Toon alle bestandssystemen en hun schijfgebruik:

`df`

- Toon alle bestandssystemen en hun schijfgebruik in een leesbaar formaat:

`df -h`

- Toon het bestandssysteem en het schijfgebruik voor het opgegeven bestand of map:

`df {{pad/naar/bestand_of_map}}`

- Neem statistieken op over het aantal beschikbare [i]-knooppunte:

`df -i`

- Toon bestandssystemen maar negeer specifieke types:

`df -x {{squashfs}} -x {{tmpfs}}`
