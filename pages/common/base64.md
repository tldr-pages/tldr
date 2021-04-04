# base64

> Encode or decode file or standard input to/from Base64, to standard output.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/base64-invocation.html>.

- Encode the contents of a file as base64 and write the result to stdout:

`base64 {{filename}}`

- Decode the base64 contents of a file to stdout:

`base64 --decode {{filename}}`

- Encode from stdin:

`{{somecommand}} | base64`

- Decode from stdin:

`{{somecommand}} | base64 --decode`
