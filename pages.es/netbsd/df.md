# df

> Muestra una visión general del uso del espacio en disco del sistema de archivos.
> Más información: <https://man.netbsd.org/NetBSD-9.3/df.1>.

- Muestra todos los sistemas de ficheros y su uso de disco usando unidades de 512 bytes:

`df`

- Utiliza palabras [h]umanas para indicar unidades (basadas en potencias de 1024):

`df -h`

- Muestra todos los campos de la(s) estructura(s) devuelta(s) por `statvfs`:

`df -G`

- Muestra el sistema de archivos y su uso del disco que contiene el archivo o directorio dado:

`df {{ruta/al/archivo_o_directorio}}`

- Incluye estadísticas sobre el número de nodos-[i] libres y utilizados:

`df -i`

- Utiliza unidades de 1024 bytes al escribir las cifras de espacio:

`df -k`

- Muestra la información de manera [P]ortable:

`df -P`
