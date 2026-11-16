# mktemp

> Create a temporary file or directory.
> More information: <https://keith.github.io/xcode-man-pages/mktemp.1.html>.

- Create an empty temporary file and print its absolute path:

`mktemp`

- Create a temporary file in a specific existing directory:

`mktemp --tmpdir="{{path/to/temporary_directory}}"`

- Use a custom path template (`X`s are replaced with random alphanumeric characters):

`mktemp {{/tmp/example.XXXXXXXX}}`

- Use a custom file name prefix:

`mktemp -t {{example}}`

- Create an empty temporary directory and print its absolute path:

`mktemp --directory`

- Create a temporary directory inside a specific existing directory:

`mktemp --directory --tmpdir="{{path/to/temporary_directory}}"`
