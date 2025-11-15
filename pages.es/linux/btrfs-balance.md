# btrfs balance

> Equilibra grupos de bloques en un sistema de archivos btrf.
> Más información: <https://btrfs.readthedocs.io/en/latest/btrfs-balance.html>.

- Muestra el estado de una operación de equilibrio en curso o pausada:

`sudo btrfs balance status {{ruta/al/sistema_de_archivos_btrfs}}`

- Equilibra todos los grupos de bloques (lento; reescribe todos los bloques en el sistema de archivos):

`sudo btrfs balance start {{ruta/al/sistema_de_archivos_btrfs}}`

- Equilibra grupos de bloques de datos que están menos del 15% utilizados, ejecutando la operación en segundo plano:

`sudo btrfs balance start --bg -dusage={{15}} {{ruta/al/sistema_de_archivos_btrfs}}`

- Equilibra un máximo de 10 bloques de metadatos con menos del 20% de utilización y al menos 1 bloque en un dispositivo dado `devid` (vea `btrfs filesystem show`):

`sudo btrfs balance start -musage={{20}},limit={{10}},devid={{devid}} {{ruta/al/sistema_de_archivos_btrfs}}`

- Convierte bloques de datos a raid6 y metadatos a raid1c3 (vea mkfs.btrfs(8) para perfiles):

`sudo btrfs balance start -dconvert={{raid6}} -mconvert={{raid1c3}} {{ruta/al/sistema_de_archivos_btrfs}}`

- Convierte bloques de datos a raid1, omitiendo bloques ya convertidos (por ejemplo, después de una operación de conversión cancelada previamente):

`sudo btrfs balance start -dconvert={{raid1}},soft {{ruta/al/sistema_de_archivos_btrfs}}`

- Cancela, pausa o reanuda una operación de equilibrio en curso o pausada:

`sudo btrfs balance {{cancelar|pausar|reanudar}} {{ruta/al/sistema_de_archivos_btrfs}}`
