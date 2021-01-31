# base64

> Codifica o decodifica file o standard input in Base64 su standard output.

- Codifica un file:

`base64 {{nome_file}}`

- Decodifica un file:

`base64 -d {{nome_file}}`

- Codifica da stdin:

`{{comando}} | base64`

- Decodifica da stdin:

`{{comando}} | base64 -d`
