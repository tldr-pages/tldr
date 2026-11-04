# lrzip

> Un programa para comprimir archivos de gran tamaño.
> Vea también: `lrunzip`, `lrztar`, `lrzuntar`.
> Más información: <https://manned.org/lrzip>.

- Comprime un archivo con LZMA: compresión lenta, descompresión rápida:

`lrzip {{ruta/al/archivo}}`

- Comprime un archivo con BZIP2: buen equilibrio entre compresión y velocidad:

`lrzip {{[-b|--bzip2]}} {{ruta/al/archivo}}`

- Comprime con ZPAQ: compresión extrema, pero muy lenta:

`lrzip {{[-z|--zpaq]}} {{ruta/al/archivo}}`

- Comprime con LZO: compresión ligera, descompresión extremadamente rápida:

`lrzip {{[-l|--lzo]}} {{ruta/al/archivo}}`

- Comprime un archivo y lo protege con contraseña o lo cifra:

`lrzip {{[-e|--encrypt]}} {{ruta/al/archivo}}`

- Especifica el número de subprocesos del procesador que se van a utilizar:

`lrzip {{[-p|--threads]}} {{8}} {{ruta/al/archivo}}`
