# mktemp

> Create a temporary file or directory.
> More information: <https://www.gnu.org/software/coreutils/mktemp>.

- Create an empty temporary file and print its absolute path:

`mktemp`

- Use a custom directory (defaults to `$TMPDIR`, or `/tmp`):

`mktemp --tmpdir={{/path/to/tempdir}}`

- Use a custom path template (`X`s are replaced with random alphanumeric characters):

`mktemp {{/tmp/example.XXXXXXXX}}`

- Use a custom file name template:

`mktemp -t {{example.XXXXXXXX}}`

- Create an empty temporary file with the given suffix and print its absolute path:

`mktemp --suffix {{.ext}}`

- Create an empty temporary directory and print its absolute path:

`mktemp --directory`
