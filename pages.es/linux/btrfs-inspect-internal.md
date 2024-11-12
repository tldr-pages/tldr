# btrfs inspect-internal

> Consulta información interna de un sistema de archivos btrfs.
> Más información: <https://btrfs.readthedocs.io/en/latest/btrfs-inspect-internal.html>.

- Imprime la información del superbloque:

`sudo btrfs inspect-internal dump-super {{ruta/a/la_partición}}`

- Imprime la información del superbloque y de todas sus copias:

`sudo btrfs inspect-internal dump-super --all {{ruta/a/la_partición}}`

- Imprime la información de los metadatos del sistema de archivos:

`sudo btrfs inspect-internal dump-tree {{ruta/a/la_partición}}`

- Imprime la lista de archivos en el inodo `n`-ésimo:

`sudo btrfs inspect-internal inode-resolve {{n}} {{ruta/al_montaje_btrfs}}`

- Imprime la lista de archivos en una dirección lógica dada:

`sudo btrfs inspect-internal logical-resolve {{dirección_lógica}} {{ruta/al_montaje_btrfs}}`

- Imprime estadísticas de los árboles de root, extent, csum y fs:

`sudo btrfs inspect-internal tree-stats {{ruta/a/la_partición}}`
