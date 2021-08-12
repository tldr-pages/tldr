# mkfs.ext4

> Creează un sistem de fişiere ext4 în interiorul unei partiţii.

- Creați un sistem de fișiere ext4 în interiorul partiției 1 pe dispozitivul b (`sdb1`):

`sudo mkfs.ext4 {{/dev/sdb1}}`

- Creați un sistem de fișiere ext4 cu o etichetă de volum:

`sudo mkfs.ext4 -L {{volume_label}} {{/dev/sdb1}}`
