# base64

> Encode or decode file or standard input to/from Base64, to standard output.

- Encode a file:

`base64 {{filename}}`

- Decode a file:

`base64 -d {{filename}}`

- Encode from `stdin`:

`{{somecommand}} | base64`

- Decode from `stdin`:

`{{somecommand}} | base64 -d`
