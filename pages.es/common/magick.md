# magick

> Crea, edita, compone o convierte entre formatos de imagen.
> Esta herramienta reemplaza a `convert` en ImageMagick 7+. Usa `magick convert` para utilizar la herramienta antigua en versiones 7+.
> Algunos subcomandos, como `mogrify`, tienen su propia documentación de uso.
> Más información: <https://imagemagick.org>.

- Convierte entre formatos de imagen:

`magick {{ruta/a/imagen_entrada.png}} {{ruta/a/imagen_salida.jpg}}`

- Redimensiona una imagen, creando una nueva copia:

`magick {{ruta/a/imagen_entrada.jpg}} -resize {{100x100}} {{ruta/a/imagen_salida.jpg}}`

- Crea un GIF a partir de todas las imágenes JPEG en el directorio actual:

`magick {{*.jpg}} {{ruta/a/imagenes.gif}}`

- Crea un patrón de tablero de ajedrez:

`magick -size {{640x480}} pattern:checkerboard {{ruta/a/tablero.png}}`

- Crea un archivo PDF a partir de todas las imágenes JPEG en el directorio actual:

`magick {{*.jpg}} -adjoin {{ruta/a/archivo.pdf}}`
