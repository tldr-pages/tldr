# mkfs.cramfs

> Creează un sistem de fişiere ROM în interiorul unei partiţii.

- Creați un sistem de fișiere ROM în interiorul partiției 1 pe dispozitivul b (`sdb1`):

`mkfs.cramfs {{/dev/sdb1}}`

- Creați un sistem de fișiere ROM cu un nume de volum:

`mkfs.cramfs -n {{volume_name}} {{/dev/sdb1}}`
