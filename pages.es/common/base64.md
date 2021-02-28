# base64

> Codifica o decodifica un archivo o la entrada estandar hacia/desde Base64, a la salida estandar.

- Codifica un archivo:

`base64 {{nombre_de_archivo}}`

- Decodifica un archivo:

`base64 -d {{nombre_de_archivo}}`

- Codifica stdin:

`{{comando}} | base64`

- Decodifica stdin:

`{{comando}} | base64 -d`
