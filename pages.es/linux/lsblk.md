# lsblk

> Lista información sobre dispositivos.
> Más información: <https://manned.org/lsblk>.

- Lista todos los dispositivos de almacenamiento en formato de árbol:

`lsblk`

- Lista también los dispositivos vacíos:

`lsblk {{[-a|--all]}}`

- Muestra la columna SIZE en bytes en lugar de un formato legible por humanos:

`lsblk {{[-b|--bytes]}}`

- Muestra información sobre los sistemas de archivos:

`lsblk {{[-f|--fs]}}`

- Usa caracteres ASCII para dibujar el árbol:

`lsblk {{[-i|--ascii]}}`

- Muestra información sobre la topología de los dispositivos de bloque:

`lsblk {{[-t|--topology]}}`

- Excluye los dispositivos indicados mediante una lista de números mayores de dispositivo separados por comas:

`lsblk {{[-e|--exclude]}} {{1,7,...}}`

- Añade información extra a la salida usando una lista de columnas separadas por comas (omite el signo `+` para mostrar solo las columnas indicadas):

`lsblk {{[-o|--output]}} +{{NAME,ROTA,SERIAL,MODEL,TRAN,TYPE,SIZE,FSTYPE,MOUNTPOINT,...}}`
