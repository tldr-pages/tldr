# bzip2

> Un compresor de archivos de clasificación por bloques.
> Vea también: `bzcat`, `bunzip2`, `bzip2recover`.
> Más información: <https://manned.org/bzip2>.

- Comprime un archivo:

`bzip2 {{ruta/al/archivo_a_comprimir}}`

- Descomprime un archivo:

`bzip2 {{[-d|--decompress]}} {{ruta/al/archivo_comprimido.bz2}}`

- Descomprime un archivo en `stdout`:

`bzip2 {{[-dc|--decompress --stdout]}} {{ruta/al/archivo_comprimido.bz2}}`

- Comprueba la integridad de cada fichero dentro del archivo comprimido:

`bzip2 {{[-t|--test]}} {{ruta/al/archivo_comprimido.bz2}}`

- Muestra la relación de compresión de cada archivo procesado con información detallada:

`bzip2 {{[-v|--verbose]}} {{ruta/al/archivo_comprimido.bz2}}`

- Descomprime un archivo sobrescribiendo los archivos existentes:

`bzip2 {{[-f|--force]}} {{ruta/al/archivo_comprimido.bz2}}`

- Muestra la ayuda:

`bzip2 {{[-h|--help]}}`
