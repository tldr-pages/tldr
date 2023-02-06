# mkfs.ext4

> Egy ext4 fájlrendszert hoz létre egy partíción belül. További információ: <https://manned.org/mkfs.ext4>.

- Létrehoz egy ext4 fájlrendszert az 1. partíción belül a b eszközön (`sdb1`):

`sudo mkfs.ext4 {{/dev/sdb1}}`

- Létrehoz egy ext4 fájlrendszert egy kötetcímkével:

`sudo mkfs.ext4 -L {{volume_label}} {{/dev/sdb1}}`
