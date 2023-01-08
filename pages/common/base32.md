# base32

> Encode or decode file or standard input to/from Base32, to standard output.
> More information: <https://www.gnu.org/software/coreutils/base32>.

- Encode a file:

`base32 {{path/to/file}}`

- Decode a file:

`base32 --decode {{path/to/file}}`

- Encode from `stdin`:

`{{somecommand}} | base32`

- Decode from `stdin`:

`{{somecommand}} | base32 --decode`
