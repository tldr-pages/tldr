# mkfs

> Crea un sistema de archivos de Linux en una partición de disco duro.
> Nota: Este comando está obsoleto, use comandos específicos de cada sistema de archivos como `mkfs.ext4` en su lugar.
> Más información: <https://manned.org/mkfs>.

- Crea un sistema de archivos ext2 de Linux en una partición:

`sudo mkfs {{/dev/sdXY}}`

- Crea un sistema de archivos de un tipo específico:

`sudo mkfs {{[-t|--type]}} {{ext4}} {{/dev/sdXY}}`

- Crea un sistema de archivos de un tipo específico y busca bloques defectuosos:

`sudo mkfs -c {{[-t|--type]}} {{ntfs}} {{/dev/sdXY}}`
