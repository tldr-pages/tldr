# mkfs.exfat

> Exfat fájlrendszert hoz létre egy partíción belül. További információ: <https://manned.org/mkfs.exfat>.

- Létrehoz egy exfat fájlrendszert az 1. partíción belül a b eszközön (`sdb1`):

`mkfs.exfat {{/dev/sdb1}}`

- Létrehoz egy fájlrendszert kötetnévvel:

`mkfs.exfat -n {{volume_name}} {{/dev/sdb1}}`

- Fájlrendszer létrehozása kötet-azonosítóval:

`mkfs.exfat -i {{volume_id}} {{/dev/sdb1}}`
