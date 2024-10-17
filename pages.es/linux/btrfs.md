# btrfs

> Un sistema de archivos basado en el principio de copia en escritura (COW) para Linux.
> Algunos subcomandos como `device` tienen su propia documentación de uso.
> Más información: <https://btrfs.readthedocs.io/en/latest/btrfs.html>.

- Muestra subvolumen:

`sudo btrfs subvolume create {{ruta/al/subvolumen}}`

- Lista subvolúmenes:

`sudo btrfs subvolume list {{ruta/al/punto_de_montaje}}`

- Muestra información sobre el uso del espacio:

`sudo btrfs filesystem df {{ruta/al/punto_de_montaje}}`

- Habilita cuota:

`sudo btrfs quota enable {{ruta/al/subvolumen}}`

- Muestra cuota:

`sudo btrfs qgroup show {{ruta/al/subvolumen}}`
