# mktemp

> Create a temporary file or directory.
> More information: <https://keith.github.io/xcode-man-pages/mktemp.1.html>.

- Create an empty temporary file and print its absolute path:

`mktemp`

- Use a custom directory (defaults to the output of `getconf DARWIN_USER_TEMP_DIR`, or `/tmp`):

`mktemp --tmpdir={{/path/to/tempdir}}`

- Use a custom path template (`X`s are replaced with random alphanumeric characters):

`mktemp {{/tmp/example.XXXXXXXX}}`

- Use a custom file name prefix:

`mktemp -t {{example}}`

- Create an empty temporary directory and print its absolute path:

`mktemp --directory`
