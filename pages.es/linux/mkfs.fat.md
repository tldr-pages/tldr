# mkfs.fat

> Crea un sistema de ficheros MS-DOS dentro de una partición.
> Más información: <https://manned.org/mkfs.fat>.

- Crea un sistema de archivos fat dentro de la partición `Y` en el dispositivo `X`:

`mkfs.fat {{/dev/sdXY}}`

- Crea un sistema de archivos con un nombre de volumen:

`mkfs.fat -n {{nombre_volumen}} {{/dev/sdXY}}`

- Crea un sistema de archivos con un identificador de volumen:

`mkfs.fat -i {{volumen_id}} {{/dev/sdXY}}`

- Utiliza 5 en lugar de 2 tablas de asignación de archivos:

`mkfs.fat -f 5 {{/dev/sdXY}}`

- Especifica el tipo de sistema de archivos:

`mkfs.fat -F {{12|16|32}} {{/dev/sdXY}}`
