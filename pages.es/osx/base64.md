# base64

> Codifica o decodifica un archivo o `stdin` a/desde base64, a `stdout` o a otro archivo.
> Más información: <https://keith.github.io/xcode-man-pages/base64.1.html>.

- Codifica un archivo a `stdout`:

`base64 {{-i|--input}} {{ruta/al/archivo}}`

- Codificar un archivo en el archivo de salida especificado:

`base64 {{-i|--input}} {{ruta/al/archivo_de_entrada}} {{-o|--output}} {{ruta/al/archivo_salida}}`

- Ajusta la salida codificada a un ancho específico (`0` desactiva el ajuste):

`base64 {{-b|--break}} {{0|76|...}} {{ruta/al/archivo}}`

- Decodifica un archivo a `stdout`:

`base64 {{-d|--decode}} {{-i|--input}} {{ruta/al/archivo}}`

- Codifica de `stdin` a `stdout`:

`{{comando}} | base64`

- Decodifica de `stdin` a `stdout`:

`{{comando}} | base64 {{-d|--decode}}`
