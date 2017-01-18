# [base32](http://man7.org/linux/man-pages/man1/base32.1.html)
> Encode or decode file or standard input, to standard output.

- Encode a file:

`base32 {{filename}}`

- Decode a file:

`base32 -d {{filename}}`

- Encode from stdin:

`{{somecommand}} | base32`

- Decode from stdin:

`{{somecommand}} | base32 -d`
