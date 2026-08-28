# mkfs.ext4

> Crée un système de fichiers ext4 à l’intérieur d’une partition.
> Plus d’informations : <https://manned.org/mkfs.ext4>.

- Crée un système de fichiers ext4 dans la partition Y sur le périphérique X :

`sudo mkfs.ext4 {{/dev/sdXY}}`

- Crée un système de fichiers ext4 avec une étiquette de volume :

`sudo mkfs.ext4 -L {{étiquette_volume}} {{/dev/sdXY}}`

- Crée un système de fichiers ext4 appartenant à un utilisateur et à un groupe spécifiques :

`sudo mkfs.ext4 -E root_owner={{uid}}:{{gid}} {{/dev/sdXY}}`
