# base64

> Encode or decode file or standard input to/from Base64, to standard output.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/base64-invocation.html>.

- Print a plaintext file's contents encoded in base64:

`base64 {{filename}}`

- Print a base64 encoded file's contents decoded to plaintext:

`base64 --decode {{filename}}`

- Encode from stdin:

`{{somecommand}} | base64`

- Decode from stdin:

`{{somecommand}} | base64 --decode`
