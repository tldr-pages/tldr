# base64

> Codifica o decodifica un archivo o la entrada estandar hacia/desde Base64, a la salida estandar.
> Más información: <https://manned.org/base64>.

- Codifica un archivo:

`base64 {{ruta/al/archivo}}`

- Ajusta la salida codificada en un ancho específico (`0` deshabilita el ajuste):

`base64 {{[-w|--wrap]}} {{0|76|...}} {{ruta/al/archivo}}`

- Decodifica un archivo:

`base64 {{[-d|--decode]}} {{ruta/al/archivo}}`

- Codifica `stdin`:

`{{comando}} | base64`

- Decodifica `stdin`:

`{{comando}} | base64 {{[-d|--decode]}}`
