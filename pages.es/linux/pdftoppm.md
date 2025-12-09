# pdftoppm

> Convierte páginas de documentos PDF al formato de imagen Pixmap portátil.
> Más información: <https://manned.org/pdftoppm>.

- Especifica el rango de páginas a convertir (N es la primera página, M es la última página):

`pdftoppm -f {{N}} -l {{M}} {{ruta/al/archivo.pdf}} {{prefijo_del_nombre_de_la_imagen}}`

- Convierte solo la primera página de un PDF:

`pdftoppm -singlefile {{ruta/al/archivo.pdf}} {{prefijo_del_nombre_de_la_imagen}}`

- Genera un archivo PBM monocromático (en lugar de un archivo PPM de color):

`pdftoppm -mono {{ruta/al/archivo.pdf}} {{prefijo_del_nombre_de_la_imagen}}`

- Genera un archivo PGM en escala de grises (en lugar de un archivo PPM de color):

`pdftoppm -gray {{ruta/al/archivo.pdf}} {{prefijo_del_nombre_de_la_imagen}}`

- Genera un archivo PNG en lugar de un archivo PPM:

`pdftoppm -png {{ruta/al/archivo.pdf}} {{prefijo_del_nombre_de_la_imagen}}`
