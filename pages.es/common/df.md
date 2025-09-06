# df

> Muestra una visión general del uso del espacio en disco del sistema de archivos.
> Más información: <https://manned.org/df.1posix>.

- Muestra todos los sistemas de ficheros y su uso de disco usando unidades de 512 bytes:

`df`

- Muestra el sistema de archivos y su uso del disco que contiene el archivo o directorio dado:

`df {{ruta/al/archivo_o_directorio}}`

- Utiliza unidades de 1024 bytes en las columnas de cifras de espacio:

`df -k`

- Muestra la información de forma portátil (formato POSIX):

`df -P`
