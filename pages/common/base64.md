# base64

> Encode or decode file or `stdin` to/from Base64, to `stdout`.
> More information: <https://www.gnu.org/software/coreutils/base64>.

- Encode the contents of a file as base64 and write the result to `stdout`:

`base64 {{path/to/file}}`

- Wrap encoded output at a specific width (`0` disables wrapping):

`base64 --wrap {{0|76|...}} {{path/to/file}}`

- Decode the base64 contents of a file and write the result to `stdout`:

`base64 --decode {{path/to/file}}`

- Encode from `stdin`:

`{{somecommand}} | base64`

- Decode from `stdin`:

`{{somecommand}} | base64 --decode`
