# magick mogrify

> Realiza operaciones en múltiples imágenes, como redimensionar, recortar, voltear y añadir efectos.
> Los cambios se aplican directamente al archivo original.
> Vea también: `magick`.
> Más información: <https://imagemagick.org/script/mogrify.php>.

- Redimensiona todas las imágenes JPEG en el directorio al 50% de su tamaño inicial:

`magick mogrify -resize {{50%}} {{*.jpg}}`

- Redimensiona todas las imágenes comenzando con `DSC` a 800x600:

`magick mogrify -resize {{800x600}} {{DSC*}}`

- Convierte todos los PNG a JPEG:

`magick mogrify -format {{jpg}} {{*.png}}`

- Redimensiona todas las imágenes JPEG en el directorio al 50% de su tamaño inicial:

`magick mogrify -modulate {{100,50}} {{*}}`

- Dobla el brillo de todos los archivos de imagen en el directorio actual:

`magick mogrify -modulate {{200}} {{*}}`

- Reduce tamaños de archivos de todas las imágenes GIF en el directorio actual reduciendo la calidad:

`magick mogrify -layers 'optimize' -fuzz {{7%}} {{*.gif}}`

- Muestra la ayuda:

`magick mogrify -help`
