# btrfs property

> Obtiene, establece o lista propiedades para un objeto de sistema de archivos BTRFS (archivos, directorios, subvolúmenes, sistemas de archivos o dispositivos).
> Más información: <https://btrfs.readthedocs.io/en/latest/btrfs-property.html>.

- Lista las propiedades disponibles (y descripciones) para el objeto btrfs dado:

`sudo btrfs property list {{ruta/al_objeto_btrfs}}`

- Obtiene todas las propiedades para el objeto btrfs dado:

`sudo btrfs property get {{ruta/al_objeto_btrfs}}`

- Obtiene la propiedad `label` para el sistema de archivos o dispositivo btrfs dado:

`sudo btrfs property get {{ruta/al_sistema_de_archivos_btrfs}} label`

- Obtiene todas las propiedades específicas del tipo de objeto para el sistema de archivos o dispositivo btrfs dado:

`sudo btrfs property get -t {{subvol|filesystem|inode|device}} {{ruta/al_sistema_de_archivos_btrfs}}`

- Establece la propiedad `compression` para un inodo btrfs dado (ya sea un archivo o un directorio):

`sudo btrfs property set {{ruta/al_inodo_btrfs}} compression {{zstd|zlib|lzo|none}}`
