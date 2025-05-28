# lvcreate

> Crea un volumen lógico en un grupo de volumen existente. Un grupo de volumen es una colección de volúmenes lógicos y físicos.
> Vea también: `lvm`.
> Más información: <https://manned.org/lvcreate>.

- Crea un volumen lógico de 10 GB en el grupo de volumen vg1:

`lvcreate {{[-L|--size]}} {{10G}} {{vg1}}`

- Crea un volumen lógico lineal de 1500 MB llamado mylv en el grupo de volumen vg1:

`lvcreate {{[-L|--size]}} {{1500}} {{[-n|--name]}} {{mylv}} {{vg1}}`

- Crea un volumen lógico llamado mylv que utiliza el 60% del espacio total del grupo de volumen vg1:

`lvcreate {{[-l|--extents]}} {{60%VG}} {{[-n|--name]}} {{mylv}} {{vg1}}`

- Crea un volumen lógico llamado mylv que utiliza todo el espacio sin asignar del grupo de volumen vg1:

`lvcreate {{[-l|--extents]}} {{100%FREE}} {{[-n|--name]}} {{mylv}} {{vg1}}`
