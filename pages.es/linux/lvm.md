# lvm

> Administración de volúmenes fisicos, grupos de volúmenes, y volúmenes lógicos mediante la terminal interactiva de Logical Volume Manager (LVM).
> Más información: <https://manned.org/lvm>.

- Inicia la terminal interactiva Logical Volume Manager:

`sudo lvm`

- Inicializa un disco o partición para ser utilizado como volumen físico:

`sudo lvm pvcreate {{/dev/sdXY}}`

- Imprime información sobre volúmenes físicos:

`sudo lvm pvdisplay`

- Crea un grupo de volumen llamado vg1 a partir del volumen físico en `/dev/sdXY`:

`sudo lvm vgcreate {{vg1}} {{/dev/sdXY}}`

- Imprime información sobre grupos de volumen:

`sudo lvm vgdisplay`

- Crea un volumen lógico con un tamaño de 10G a partir del grupo de volumen vg1:

`sudo lvm lvcreate {{[-L|--size]}} {{10G}} {{vg1}}`

- Imprime información sobre volúmenes lógicos:

`sudo lvm lvdisplay`

- Imprime ayuda para un comando específico:

`lvm help {{command}}`
