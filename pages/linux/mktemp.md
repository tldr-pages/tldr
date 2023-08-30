# mktemp

> Create a temporary file or directory.
> Note that examples here all assume `$TMPDIR` is unset.
> More information: <https://www.gnu.org/software/autogen/mktemp.html>.

- Create an empty temporary file in `/tmp/` and print its absolute path:

`mktemp`

- Create a temporary directory in `/tmp/` and print its absolute path:

`mktemp --directory`

- Create an empty temporary file at the specified path, with `X`s replaced with random alphanumeric characters, and print its path:

`mktemp "{{path/to/file_XXXXX_name}}"`

- Create an empty temporary file in `/tmp/` with the specified name, with `X`s replaced with random alphanumeric characters, and print its path:

`mktemp -t "{{file_XXXXX_name}}"`
