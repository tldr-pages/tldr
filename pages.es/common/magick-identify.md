# magick identify

> Describe el formato y las características de los archivos de imagen.
> Vea también: `magick`.
> Más información: <https://imagemagick.org/script/identify.php>.

- Describe el formato y las características básicas de una imagen:

`magick identify {{ruta/a/la/imagen}}`

- Describe el formato y las características de una imagen detalladamente:

`magick identify -verbose {{ruta/a/la/imagen}}`

- Recopila las dimensiones de todos los archivos JPEG en el directorio actual y los guarda en un archivo CSV:

`magick identify -format "{{%f,%w,%h\n}}" {{*.jpg}} > {{ruta/al/archivo.csv}}`
