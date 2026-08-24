# btrfs

> Un sistema de archivos basado en el principio de copia en escritura (COW) para Linux.
> Algunos subcomandos como `device` tienen su propia documentación de uso.
> Más información: <https://btrfs.readthedocs.io/en/latest/btrfs.html>.

- Muestra subvolumen:

`sudo btrfs {{[su|subvolume]}} {{[c|create]}} {{ruta/al/subvolumen}}`

- Lista subvolúmenes:

`sudo btrfs {{[su|subvolume]}} {{[l|list]}} {{ruta/al/punto_de_montaje}}`

- Muestra información sobre el uso del espacio:

`sudo btrfs {{[f|filesystem]}} df {{ruta/al/punto_de_montaje}}`

- Habilita cuota:

`sudo btrfs {{[qu|quota]}} {{[e|enable]}} {{ruta/al/subvolumen}}`

- Muestra cuota:

`sudo btrfs {{[qg|qgroup]}} {{[s|show]}} {{ruta/al/subvolumen}}`
