# df

> Entrega información general del uso de espacio en disco del sistema de archivos.
> Más información: <https://manned.org/df.1posix>.

- Muestra todos los sistemas de archivos y sus usos de disco:

`df`

- Muestra todos los sistemas de archivos y sus usos de disco en formato legible para humanos:

`df -h`

- Muestra el sistema de archivos que contiene determinado archivo o directorio y su uso de disco:

`df {{ruta/al/archivo_o_directorio}}`

- Muestra estadísticas sobre el número de inodos libres:

`df -i`

- Muestra sistemas de archivos excluyendo los tipos especificados:

`df -x {{squashfs}} -x {{tmpfs}}`
