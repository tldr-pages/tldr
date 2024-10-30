# xz

> Comprime o descomprime archivos XZ y LZMA.
> Más información: <https://manned.org/xz>.

- Comprime un archivo usando xz:

`xz {{ruta/al/archivo}}`

- Descomprime un archivo XZ:

`xz --decompress {{ruta/al/archivo.xz}}`

- Comprime un archivo usando LZMA:

`xz --format=lzma {{ruta/al/archivo}}`

- Descomprime un archivo LZMA:

`xz --decompress --format=lzma {{ruta/al/archivo.lzma}}`

- Descomprime un archivo y escribe a `stdout` (implica `--keep`):

`xz --decompress --stdout {{ruta/al/archivo.xz}}`

- Comprime un archivo, pero no borra el original:

`xz --keep {{ruta/al/archivo}}`

- Comprime un archivo con la compresión más rápida:

`xz -0 {{ruta/al/archivo}}`

- Comprime un archivo con la mejor compresión:

`xz -9 {{ruta/al/archivo}}`
