# basenc

> Encode or decode file or standard input using a specified encoding, to standard output.
> More information: <https://www.gnu.org/software/coreutils/basenc>.

- Encode a file with base64 encoding:

`basenc --base64 {{path/to/file}}`

- Decode a file with base64 encoding:

`basenc --decode --base64 {{path/to/file}}`

- Encode from `stdin` with base32 encoding with 42 columns:

`{{command}} | basenc --base32 -w42`

- Encode from `stdin` with base32 encoding:

`{{command}} | basenc --base32`
