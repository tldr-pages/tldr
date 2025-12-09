# zstd

> Comprime o descomprime archivos con compresión Zstandard.
> Más información: <https://github.com/facebook/zstd>.

- Comprime un archivo en un nuevo archivo con el sufijo `.zst`:

`zstd {{ruta/al/archivo}}`

- Descomprime un archivo:

`zstd --decompress {{ruta/al/archivo.zst}}`

- Descomprime a la salida estándar `stdout`:

`zstd --decompress --stdout {{ruta/al/archivo.zst}}`

- Comprime un archivo especificando el nivel de compresión, donde 1=más rápido, 19=más lento y 3=predeterminado:

`zstd -{{nivel}} {{ruta/al/archivo}}`

- Desbloquea niveles de compresión superiores (hasta 22) utilizando más memoria (tanto para compresión como descompresión):

`zstd --ultra -{{nivel}} {{ruta/al/archivo}}`
