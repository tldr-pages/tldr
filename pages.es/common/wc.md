# wc

> Cuenta líneas, palabras, caracteres, etc.
> Más información: <https://www.man7.org/linux/man-pages/man1/wc.1.html>

- Cuenta las líneas en un archivo:

`wc -l {{ruta/al/archivo}}`

- Cuenta las palabras en un archivo:

`wc -w {{ruta/al/archivo}}`

- Cuenta caracteres (bytes) en un archivo:

`wc -c {{ruta/al/archivo}}`

- Cuenta caracteres en un archivo (tomando sets de caracteres multi-byte en cuenta):

`wc -m {{ruta/al/archivo}}`

- Usa la entrada estandar para contar líneas, palabras o caracteres (bytes), en ese orden:

`{{find .}} | wc`
