# readelf

> Az ELF fájlokkal kapcsolatos információk megjelenítése. További információ: <http://man7.org/linux/man-pages/man1/readelf.1.html>.

- Az ELF-fájlra vonatkozó összes információ megjelenítése:

`readelf -all {{path/to/binary}}`

- Az ELF-fájlban található összes fejléc megjelenítése:

`readelf --headers {{path/to/binary}}`

- Az ELF-fájl szimbólumtábla szakaszának bejegyzéseinek megjelenítése, ha van benne szimbólumtábla:

`readelf --symbols {{path/to/binary}}`

- A fájl elején található ELF fejlécben szereplő információk megjelenítése:

`readelf --file-header {{path/to/binary}}`
