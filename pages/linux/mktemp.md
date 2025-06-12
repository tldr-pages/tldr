# mktemp

> Create a temporary file or directory.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/mktemp-invocation.html>.

- Create an empty temporary file and print its absolute path:

`mktemp`

- Use a custom directory (defaults to `$TMPDIR`, or `/tmp`):

`mktemp {{[-p |--tmpdir=]}}{{/path/to/tempdir}}`

- Use a custom path template (`X`s are replaced with random alphanumeric characters):

`mktemp {{/tmp/example.XXXXXXXX}}`

- Use a custom file name template:

`mktemp -t {{example.XXXXXXXX}}`

- Create an empty temporary file with the given suffix and print its absolute path:

`mktemp --suffix {{.ext}}`

- Create an empty temporary directory and print its absolute path:

`mktemp {{[-d|--directory]}}`

- Print the name of a temporary file or directory without actually creating it:

`mktemp {{[-u|--dry-run]}}`
