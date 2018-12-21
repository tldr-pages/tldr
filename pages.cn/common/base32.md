# base32

> Encode or decode file or standard input, to standard output.

- Encode a file:

`base32 {{filename}}`

- Decode a file:

`base32 -d {{filename}}`

- Encode from stdin:

`{{somecommand}} | base32`

- Decode from stdin:

`{{somecommand}} | base32 -d`
