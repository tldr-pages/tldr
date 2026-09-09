# mkfs.exfat

> Crée un système de fichiers exfat à l’intérieur d’une partition.
> Plus d'informations : <https://manned.org/mkfs.exfat>.

- Crée un système de fichiers exfat dans la partition Y sur le périphérique X :

`sudo mkfs.exfat {{/dev/sdXY}}`

- Crée un système de fichiers avec un nom de volume :

`sudo mkfs.exfat {{[-L|--volume-label]}} {{nom_volume}} {{/dev/sdXY}}`

- Crée un système de fichiers avec un identifiant de volume :

`sudo mkfs.exfat {{[-U|--volume-guid]}} {{id_volume}} {{/dev/sdXY}}`
