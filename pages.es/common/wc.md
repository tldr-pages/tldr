# wc

> Cuenta líneas, palabras, o bytes.
> Más información: <https://www.gnu.org/software/coreutils/wc>

- Cuenta las líneas en un archivo:

`wc -l {{ruta/al/archivo}}`

- Cuenta las palabras en un archivo:

`wc -w {{ruta/al/archivo}}`

- Cuenta caracteres (bytes) en un archivo:

`wc -c {{ruta/al/archivo}}`

- Cuenta caracteres en un archivo (considerando los caracteres de varios bytes):

`wc -m {{ruta/al/archivo}}`

- Usa la entrada estandar para contar líneas, palabras o caracteres (bytes), en ese orden:

`{{find .}} | wc`
