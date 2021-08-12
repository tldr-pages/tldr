# mkfs.ntfs

> Creează un sistem de fişiere NTFS în interiorul unei partiţii.

- Creați un sistem de fișiere NTFS în interiorul partiției 1 pe dispozitivul b (`sdb1`):

`mkfs.ntfs {{/dev/sdb1}}`

- Creați un sistem de fișiere cu o etichetă de volum:

`mkfs.ntfs -L {{volume_label}} {{/dev/sdb1}}`

- Creați un sistem de fișiere cu UUID specific:

`mkfs.ntfs -U {{UUID}} {{/dev/sdb1}}`
