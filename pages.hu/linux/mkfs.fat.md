# mkfs.fat

> MS-DOS fájlrendszert hoz létre egy partíción belül. További információ: <https://manned.org/mkfs.fat>.

- Fat fájlrendszer létrehozása az 1. partíción belül a b eszközön (`sdb1`):

`mkfs.fat {{/dev/sdb1}}`

- Létrehoz egy fájlrendszert kötetnévvel:

`mkfs.fat -n {{volume_name}} {{/dev/sdb1}}`

- Fájlrendszer létrehozása kötet-azonosítóval:

`mkfs.fat -i {{volume_id}} {{/dev/sdb1}}`

- Használjon 5 helyett 2 fájlkiosztási táblát:

`mkfs.fat -f 5 {{/dev/sdb1}}`
