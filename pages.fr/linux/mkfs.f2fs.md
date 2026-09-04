# mkfs.f2fs

> Crée un système de fichiers F2FS à l’intérieur d’une partition.
> Plus d'informations : <https://manned.org/mkfs.f2fs>.

- Crée un système de fichiers F2FS dans la partition Y sur le périphérique X :

`sudo mkfs.f2fs {{/dev/sdXY}}`

- Crée un système de fichiers F2FS avec une étiquette de volume :

`sudo mkfs.f2fs -l {{étiquette_volume}} {{/dev/sdXY}}`
