# mkfs.xfs

> Crée un système de fichiers XFS à l’intérieur d’une partition.
> Plus d’informations : <https://manned.org/mkfs.xfs>.

- Crée un système de fichiers XFS dans la partition Y du périphérique X :

`sudo mkfs.xfs {{/dev/sdXY}}`

- Crée un système de fichiers XFS avec une étiquette de volume :

`sudo mkfs.xfs -L {{volume_label}} {{/dev/sdXY}}`
