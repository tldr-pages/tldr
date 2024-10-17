# btrfs restore

> Intenta recuperar archivos de un sistema de archivos btrfs dañado.
> Más información: <https://btrfs.readthedocs.io/en/latest/btrfs-restore.html>.

- Restaura todos los archivos de un sistema de archivos btrfs a un directorio dado:

`sudo btrfs restore {{ruta/al_dispositivo_btrfs}} {{ruta/al_directorio_destino}}`

- Lista (sin escribir) los archivos que se van a restaurar de un sistema de archivos btrfs:

`sudo btrfs restore --dry-run {{ruta/al_dispositivo_btrfs}} {{ruta/al_directorio_destino}}`

- Restaura archivos que coincidan con una expresión regular dada (insensible a mayúsculas) de un sistema de archivos btrfs (todos los directorios padres de los archivos de destino también deben coincidir):

`sudo btrfs restore --path-regex {{regex}} -c {{ruta/al_dispositivo_btrfs}} {{ruta/al_directorio_destino}}`

- Restaura archivos de un sistema de archivos btrfs usando un `bytenr` específico del árbol raíz (ver `btrfs-find-root`):

`sudo btrfs restore -t {{bytenr}} {{ruta/al_dispositivo_btrfs}} {{ruta/al_directorio_destino}}`

- Restaura archivos de un sistema de archivos btrfs (junto con metadatos, atributos extendidos y enlaces simbólicos), sobrescribiendo archivos en el destino:

`sudo btrfs restore --metadata --xattr --symlinks --overwrite {{ruta/al_dispositivo_btrfs}} {{ruta/al_directorio_destino}}`
