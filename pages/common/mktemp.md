# mktemp

> Create a temporary file or directory.
> More information: <https://man.openbsd.org/mktemp.1>.

- Create an empty temporary file and print its absolute path:

`mktemp`

- Use a custom directory if `$TMPDIR` is not set (the default is platform-dependent, but usually `/tmp`):

`mktemp -p /{{path/to/temporary_directory}}`

- Use a custom path template (`X`s are replaced with random alphanumeric characters):

`mktemp {{/tmp/example.XXXXXXXX}}`

- Use a custom file name template:

`mktemp -t {{example.XXXXXXXX}}`

- Create an empty temporary directory and print its absolute path:

`mktemp -d`
