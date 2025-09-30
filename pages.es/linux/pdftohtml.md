# pdftohtml

> Convierte archivos PDF a HTML, XML e imágenes PNG.
> Más información: <https://manned.org/pdftohtml>.

- Convierte un archivo PDF en un archivo HTML:

`pdftohtml {{ruta/al/archivo.pdf}} {{ruta/al/archivo_resultado.html}}`

- Ignora imágenes en el archivo PDF:

`pdftohtml -i {{ruta/al/archivo.pdf}} {{ruta/al/archivo_resultado.html}}`

- Genera un único archivo HTML que incluye todas las páginas PDF:

`pdftohtml -s {{ruta/al/archivo.pdf}} {{ruta/al/archivo_resultado.html}}`

- Convierte un archivo PDF en un archivo XML:

`pdftohtml -xml {{ruta/al/archivo.pdf}} {{ruta/al/archivo_resultado.xml}}`
