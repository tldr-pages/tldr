# mkfs.cramfs

> ROM fájlrendszert hoz létre egy partíción belül. További információ: <https://manned.org/mkfs.cramfs>.

- ROM fájlrendszer létrehozása az 1. partíción belül a b eszközön (`sdb1`):

`mkfs.cramfs {{/dev/sdb1}}`

- ROM fájlrendszer létrehozása kötetnévvel:

`mkfs.cramfs -n {{volume_name}} {{/dev/sdb1}}`
