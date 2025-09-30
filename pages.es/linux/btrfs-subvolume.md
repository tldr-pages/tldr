# btrfs subvolume

> Gestiona subvolúmenes e imágenes instantáneas de btrfs.
> Más información: <https://btrfs.readthedocs.io/en/latest/btrfs-subvolume.html>.

- Crea un nuevo subvolumen vacío:

`sudo btrfs subvolume create {{ruta/al/nuevo_subvolumen}}`

- Lista todos los subvolúmenes e imágenes instantáneas en el sistema de archivos especificado:

`sudo btrfs subvolume list {{ruta/al_sistema_de_archivos_btrfs}}`

- Elimina un subvolumen:

`sudo btrfs subvolume delete {{ruta/al_subvolumen}}`

- Crea una imagen instantánea de solo lectura de un subvolumen existente:

`sudo btrfs subvolume snapshot -r {{ruta/al_subvolumen_origen}} {{ruta/al_destino}}`

- Crea una imagen instantánea de lectura y escritura de un subvolumen existente:

`sudo btrfs subvolume snapshot {{ruta/al_subvolumen_origen}} {{ruta/al_destino}}`

- Muestra información detallada sobre un subvolumen:

`sudo btrfs subvolume show {{ruta/al_subvolumen}}`
