# isoinfo

> Segédprogramok az ISO lemezképek dömpingjéhez és ellenőrzéséhez. További információ: <https://manned.org/isoinfo>.

- Az ISO-lemezképben szereplő összes fájl listázása:

`isoinfo -f -i {{path/to/image.iso}}`

- E\[x\]nyomoz ki egy adott fájlt egy ISO-képből, és elküldi a `stdout`:

`isoinfo -i {{path/to/image.iso}} -x {{/PATH/TO/FILE/INSIDE/ISO.EXT}}`

- ISO lemezkép fejléc-információinak megjelenítése:

`isoinfo -d -i {{path/to/image.iso}}`
