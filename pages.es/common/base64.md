# base64

> Codifica o decodifica un archivo o la entrada estandar hacia/desde Base64, a la salida estandar.
> Más información: <https://www.gnu.org/software/coreutils/base64>.

- Codifica un archivo:

`base64 {{nombre_de_archivo}}`

- Decodifica un archivo:

`base64 --decode {{nombre_de_archivo}}`

- Codifica `stdin`:

`{{comando}} | base64`

- Decodifica `stdin`:

`{{comando}} | base64 --decode`
