# blkid

> Lista todas las particiones reconocidas y su identificador único universal (UUID).
> Más información: <https://manned.org/blkid>.

- Lista todas las particiones:

`sudo blkid`

- Lista todas las particiones en una tabla, incluidos los puntos de montaje actuales:

`sudo blkid {{[-o|--output]}} list`

- Obtiene el UUID del sistema de archivos en una partición:

`sudo blkid {{[-s|--match-tag]}} UUID {{[-o|--output]}} value {{/dev/sdXY}}`
