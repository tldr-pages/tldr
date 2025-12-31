# partclone

> Copia y restaura particiones desde y hacia una imagen sin tener en cuenta los bloques vacíos.
> Más información: <https://manned.org/partclone>.

- Copia una partición en una imagen:

`sudo partclone.{{ext4|btrfs|fat32|xfs|...}} {{[-c|--clone]}} {{[-s|--source]}} {{/dev/sdXY}} {{[-o|--output]}} {{ruta/a/copia.img}}`

- Restaura una partición desde una imagen:

`sudo partclone.{{ext4|btrfs|fat32|xfs|...}} {{[-c|--clone]}} {{[-s|--source]}} {{ruta/a/copia.img}} {{[-o|--output]}} {{/dev/sdXY}}`

- Muestra la ayuda:

`partclone.{{ext4|btrfs|fat32|xfs|...}} {{[-h|--help]}}`
