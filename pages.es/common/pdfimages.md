# pdfimages

> Utilidad para extraer imágenes de archivos PDF.
> Más información: <https://manned.org/pdfimages>.

- Extrae todas las imágenes de un archivo PDF y las guarda como PNGs:

`pdfimages -png {{ruta/al/archivo.pdf}} {{prefijo_nombre_archivo}}`

- Extrae imágenes de las páginas 3 a 5:

`pdfimages -f {{3}} -l {{5}} {{ruta/al/archivo.pdf}} {{prefijo_nombre_archivo}}`

- Extrae imágenes de un archivo PDF e incluye el número de página en los nombres de los archivos de salida:

`pdfimages -p {{ruta/al/archivo.pdf}} {{prefijo_nombre_archivo}}`

- Muestra información sobre todas las imágenes de un archivo PDF:

`pdfimages -list {{ruta/al/archivo.pdf}}`
