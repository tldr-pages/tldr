# hdiutil

> Utilidad para crear y gestionar imágenes de disco.
> Más información: <https://keith.github.io/xcode-man-pages/hdiutil.1.html>.

- Monta una imagen:

`hdiutil attach {{ruta/al/archivo_de_imagen}}`

- Desmonta una imagen:

`hdiutil detach /Volumes/{{archivo_de_volumen}}`

- Muestra las imágenes montadas:

`hdiutil info`

- Crea una imagen ISO a partir del contenido de un directorio:

`hdiutil makehybrid -o {{ruta/al/archivo_de_salida}} {{ruta/al/directorio}}`
