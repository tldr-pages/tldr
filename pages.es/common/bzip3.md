# bzip3

> Un eficiente compresor estadístico de archivos.
> Más información: <https://manned.org/bzip3>.

- Comprime un archivo:

`bzip3 {{ruta/al/archivo_a_comprimir}}`

- Descomprime un archivo:

`bzip3 {{[-d|--decode]}} {{ruta/al/archivo_comprimido.bz3}}`

- Descomprime un archivo en `stdout`:

`bzip3 {{[-dc|--decode --stdout]}} {{ruta/al/archivo_comprimido.bz3}}`

- Comprueba la integridad de cada fichero dentro del archivo comprimido:

`bzip3 {{[-t|--test]}} {{ruta/al/archivo_comprimido.bz3}}`

- Muestra la relación de compresión de cada archivo procesado con información detallada:

`bzip3 {{[-v|--verbose]}} {{ruta/al/archivo_comprimido.bz3}}`

- Descomprime un archivo sobrescribiendo los archivos existentes:

`bzip3 {{[-d|--decode]}} {{[-f|--force]}} {{ruta/al/archivo_comprimido.bz3}}`

- Muestra la ayuda:

`bzip3 {{[-h|--help]}}`
