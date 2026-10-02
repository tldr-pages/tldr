# lrztar

> Una herramienta de encapsulado para `lrzip` que simplifica la compresión de directorios.
> Vea también: `tar`, `lrzuntar`, `lrunzip`.
> Más información: <https://manned.org/lrztar>.

- Archiva un directorio con `tar` y, a continuación, comprimirlo:

`lrztar {{ruta/al/directorio}}`

- Igual que arriba, pero con ZPAQ (compresión extrema, aunque muy lenta):

`lrztar {{[-z|--zpaq]}} {{ruta/al/directorio}}`

- Especifica el archivo de salida:

`lrztar {{[-o|--outfile]}} {{ruta/al/archivo}} {{ruta/al/directorio}}`

- Anula el número de subprocesos del procesador que se van a utilizar:

`lrztar {{[-p|--threads]}} {{8}} {{ruta/al/directorio}}`

- Obliga la sobrescritura de los archivos existentes:

`lrztar {{[-f|--force]}} {{ruta/al/directorio}}`
