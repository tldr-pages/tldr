# basenc

> Codifica o decodifica un archivo o `stdin` usando una codificación especificada, a `stdout`.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/basenc-invocation.html>.

- Codifica un archivo con codificación base64:

`basenc --base64 {{ruta/a/archivo}}`

- Descifra un archivo con codificación base64:

`basenc {{[-d|--decode]}} --base64 {{ruta/a/archivo}}`

- Codifica desde `stdin` con codificación base32 con 42 columnas:

`{{comando}} | basenc --base32 {{[-w|--wrap]}} 42`

- Codifica desde `stdin` con codificación base32:

`{{comando}} | basenc --base32`
