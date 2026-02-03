# btrfs subvolume

> Gestiona subvolúmenes e imágenes instantáneas de btrfs.
> Más información: <https://btrfs.readthedocs.io/en/latest/btrfs-subvolume.html>.

- Crea un nuevo subvolumen vacío:

`sudo btrfs {{[su|subvolume]}} {{[c|create]}} {{ruta/al/nuevo_subvolumen}}`

- Lista todos los subvolúmenes e imágenes instantáneas en el sistema de archivos especificado:

`sudo btrfs {{[su|subvolume]}} {{[l|list]}} {{ruta/al_sistema_de_archivos_btrfs}}`

- Elimina un subvolumen:

`sudo btrfs {{[su|subvolume]}} {{[d|delete]}} {{ruta/al_subvolumen}}`

- Crea una imagen instantánea de solo lectura de un subvolumen existente:

`sudo btrfs {{[su|subvolume]}} {{[sn|snapshot]}} -r {{ruta/al_subvolumen_origen}} {{ruta/al_destino}}`

- Crea una imagen instantánea de lectura y escritura de un subvolumen existente:

`sudo btrfs {{[su|subvolume]}} {{[sn|snapshot]}} {{ruta/al_subvolumen_origen}} {{ruta/al_destino}}`

- Muestra información detallada sobre un subvolumen:

`sudo btrfs {{[su|subvolume]}} {{[sh|show]}} {{ruta/al_subvolumen}}`
