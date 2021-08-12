# mkfs.exfat

> Creează un sistem de fișiere exfat în interiorul unei partiții.

- Creați un sistem de fișiere exfat în interiorul partiției 1 pe dispozitivul b (`sdb1`):

`mkfs.exfat {{/dev/sdb1}}`

- Creați un sistem de fișiere cu un nume de volum:

`mkfs.exfat -n {{volume_name}} {{/dev/sdb1}}`

- Creați un sistem de fișiere cu un id de volum:

`mkfs.exfat -i {{volume_id}} {{/dev/sdb1}}`
