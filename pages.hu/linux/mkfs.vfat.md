# mkfs.vfat

> MS-DOS fájlrendszert hoz létre egy partíción belül. További információ: <https://manned.org/mkfs.vfat>.

- Létrehoz egy vfat fájlrendszert az 1. partíción belül a b eszközön (`sdb1`):

`mkfs.vfat {{/dev/sdb1}}`

- Létrehozza a fájlrendszert egy kötetnévvel:

`mkfs.vfat -n {{volume_name}} {{/dev/sdb1}}`

- Dateirendszer létrehozása kötet-azonosítóval:

`mkfs.vfat -i {{volume_id}} {{/dev/sdb1}}`

- Használjon 5 helyett 2 fájlkiosztási táblát:

`mkfs.vfat -f 5 {{/dev/sdb1}}`
