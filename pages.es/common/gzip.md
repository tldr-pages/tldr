# gzip

> Comprime/descomprime archivos con compresión `gzip` (LZ77).
> Más información: <https://www.gnu.org/software/gzip/manual/gzip.html>.

- Comprime un archivo, reemplazándolo con un archivo `gzip`:

`gzip {{ruta/al/archivo}}`

- Descomprime un archivo, reemplazándolo con la versión original sin comprimir:

`gzip {{[-d|--decompress]}} {{ruta/al/archivo.gz}}`

- Muestra el nombre y el porcentaje de reducción de cada archivo comprimido:

`gzip {{[-v|--verbose]}} {{ruta/al/archivo.gz}}`

- Comprime un archivo, conservando el archivo original:

`gzip {{[-k|--keep]}} {{ruta/al/archivo}}`

- Comprime un archivo, especificando el nombre del archivo de salida:

`gzip {{[-c|--stdout]}} {{ruta/al/archivo}} > {{ruta/al/archivo_comprimido.gz}}`

- Descomprime un archivo `gzip` especificando el nombre del archivo de salida:

`gzip {{[-cd|--stdout --decompress]}} {{ruta/al/archivo.gz}} > {{ruta/al/archivo_descomprimido}}`

- Especifica el nivel de compresión. 1 es el más rápido (baja compresión), 9 es el más lento (alta compresión), 6 es el predeterminado:

`gzip -{{1..9}} {{[-c|--stdout]}} {{ruta/al/archivo}} > {{ruta/al/archivo_comprimido.gz}}`

- Lista el contenido de un archivo comprimido:

`gzip {{[-l|--list]}} {{ruta/al/archivo.txt.gz}}`
