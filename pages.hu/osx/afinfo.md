# afinfo

> Audiofájl metaadat-elemző OS X-hez. Az OS X beépített parancsa. További információ: <https://ss64.com/osx/afinfo.html>.

- Egy adott hangfájl információinak megjelenítése:

`afinfo {{path/to/file}}`

- Kiírja az audiofájl egysoros leírását:

`afinfo --brief {{path/to/file}}`

- Metaadat-információk és a hangfájl InfoDictionary tartalmának nyomtatása:

`afinfo --info {{path/to/file}}`

- Kimenet nyomtatása XML formátumban:

`afinfo --xml {{path/to/file}}`

- A hangfájlra vonatkozó figyelmeztetések nyomtatása, ha vannak:

`afinfo --warnings {{path/to/file}}`

- Súgó megjelenítése a teljes használathoz:

`afinfo --help`
