# btrfs filesystem

> Gestiona sistemas de archivos btrfs.
> Más información: <https://btrfs.readthedocs.io/en/latest/btrfs-filesystem.html>.

- Muestra el uso del sistema de archivos (de manera opcional ejecutarlo como root para mostrar información detallada):

`btrfs filesystem usage {{ruta/al_montaje_btrfs}}`

- Muestra el uso por dispositivos individuales:

`sudo btrfs filesystem show {{ruta/al_montaje_btrfs}}`

- Desfragmenta un único archivo en un sistema de archivos btrfs (evita mientras un agente de deduplicación esté en ejecución):

`sudo btrfs filesystem defragment -v {{ruta/al/archivo}}`

- Desfragmenta un directorio recursivamente (no cruza los límites de subvolúmenes):

`sudo btrfs filesystem defragment -v -r {{ruta/al/directorio}}`

- Fuerza la sincronización de bloques de datos no escritos en disco(s):

`sudo btrfs filesystem sync {{ruta/al_montaje_btrfs}}`

- Resume el uso del disco para los archivos en un directorio de manera recursiva:

`sudo btrfs filesystem du --summarize {{ruta/al/directorio}}`
