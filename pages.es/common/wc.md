# wc

> Cuenta líneas, palabras, y bytes.
> Más información: <https://www.gnu.org/software/coreutils/wc>.

- Cuenta todas las líneas en un archivo:

`wc --lines {{ruta/al/archivo}}`

- Cuenta todas las palabras en un archivo:

`wc --words {{ruta/al/archivo}}`

- Cuenta todos los bytes en un archivo:

`wc --bytes {{ruta/al/archivo}}`

- Cuenta todos los caracteres en un archivo (considerando los caracteres de varios bytes):

`wc --chars {{ruta/al/archivo}}`

- Cuenta todas las líneas, palabras y bytes desde `stdin`:

`{{find .}} | wc`

- Cuenta la longitud de la línea más larga en número de caracteres:

`wc --max-line-length {{ruta/al/archivo}}`
