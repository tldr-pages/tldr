# base32

> Encode or decode file or standard input to/from Base32, to standard output.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/base32-invocation.html>.

- Encode a file:

`base32 {{filename}}`

- Decode a file:

`base32 --decode {{filename}}`

- Encode from stdin:

`{{somecommand}} | base32`

- Decode from stdin:

`{{somecommand}} | base32 --decode`
