# qmv

> Mueve archivos y directorios usando el editor de texto predeterminado para definir los nombres de archivos.
> Más información: <https://www.nongnu.org/renameutils/>.

- Mueve un solo archivo (abre un editor con el nombre de archivo fuente a la izquierda y el nombre de archivo de destino a la derecha):

`qmv {{archivo_original}}`

- Mueve múltiples archivos JPEG:

`qmv {{*.jpg}}`

- Mueve múltiples directorios:

`qmv -d {{ruta/al/directorio1}} {{ruta/al/directorio2}} {{ruta/al/directorio3}}`

- Mueve todos los archivos y directorios dentro de un directorio:

`qmv --recursive {{ruta/al/directorio}}`

- Mueve archivos, pero cambia las posiciones de la fuente y los nombres de archivo de destino en el editor:

`qmv --option swap {{*.jpg}}`

- Renombra todos los archivos y carpetas en el directorio actual, pero muestra solo los nombres de archivo de destino en el editor (puedes pensar en ello como una especie de modo simple):

`qmv --format=do .`
