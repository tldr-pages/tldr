# base32

> Codifica o decodifica file o standard input in Base32 su standard output.

- Codifica un file:

`base32 {{nome_file}}`

- Decodifica un file:

`base32 -d {{nome_file}}`

- Codifica da stdin:

`{{comando}} | base32`

- Decodifica da stdin:

`{{comando}} | base32 -d`
