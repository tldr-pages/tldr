# findmnt

> Keresse meg a fájlrendszert. További információ: <https://manned.org/findmnt>.

- Az összes csatlakoztatott fájlrendszer listázása:

`findmnt`

- Egy eszköz keresése:

`findmnt {{/dev/sdb1}}`

- Szerelési pont keresése:

`findmnt {{/}}`

- Bizonyos típusú fájlrendszerek keresése:

`findmnt -t {{ext4}}`

- Speciális címkével rendelkező fájlrendszerek keresése:

`findmnt LABEL={{BigStorage}}`
