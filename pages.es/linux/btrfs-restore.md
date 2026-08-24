# btrfs restore

> Intenta recuperar archivos de un sistema de archivos btrfs dañado.
> Más información: <https://btrfs.readthedocs.io/en/latest/btrfs-restore.html>.

- Restaura todos los archivos de un sistema de archivos btrfs a un directorio dado:

`sudo btrfs {{[rest|restore]}} {{ruta/al_dispositivo_btrfs}} {{ruta/al_directorio_destino}}`

- Lista (sin escribir) los archivos que se van a restaurar de un sistema de archivos btrfs:

`sudo btrfs {{[rest|restore]}} {{[-D|--dry-run]}} {{ruta/al_dispositivo_btrfs}} {{ruta/al_directorio_destino}}`

- Restaura archivos que coincidan con una `regex` dada (insensible a mayúsculas) de un sistema de archivos btrfs (todos los directorios padres de los archivos de destino también deben coincidir):

`sudo btrfs {{[rest|restore]}} --path-regex {{regex}} -c {{ruta/al_dispositivo_btrfs}} {{ruta/al_directorio_destino}}`

- Restaura archivos de un sistema de archivos btrfs usando un `bytenr` específico del árbol raíz (ver `btrfs-find-root`):

`sudo btrfs {{[rest|restore]}} -t {{bytenr}} {{ruta/al_dispositivo_btrfs}} {{ruta/al_directorio_destino}}`

- Restaura archivos de un sistema de archivos btrfs (junto con metadatos, atributos extendidos y enlaces simbólicos), sobrescribiendo archivos en el destino:

`sudo btrfs {{[rest|restore]}} {{[-m|--metadata]}} {{[-x|--xattr]}} {{[-S|--symlinks]}} {{[-o|--overwrite]}} {{ruta/al_dispositivo_btrfs}} {{ruta/al_directorio_destino}}`
