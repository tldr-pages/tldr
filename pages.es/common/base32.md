# base32

> Codifica o decodifica un archivo o la entrada estandar hacia/desde Base32, a la salida estandar.
> Más información: <https://manned.org/base32>.

- Codifica un archivo:

`base32 {{ruta/al/archivo}}`

- Ajuste la salida codificada en un ancho específico (`0` deshabilita el ajuste):

`base32 {{[-w|--wrap]}} {{0|76|...}} {{ruta/al/archivo}}`

- Decodifica un archivo:

`base32 {{[-d|--decode]}} {{ruta/al/archivo}}`

- Codifica `stdin`:

`{{comando}} | base32`

- Decodifica `stdin`:

`{{comando}} | base32 {{[-d|--decode]}}`
