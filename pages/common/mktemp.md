# mktemp

> Create a temporary file or directory.
> More information: <https://manned.org/mktemp.1>.

- Create an empty temporary file and print the absolute path to it:

`mktemp`

- Create an empty temporary file with a given suffix and print the absolute path to file:

`mktemp --suffix "{{.ext}}"`

- Create a temporary directory and print the absolute path to it:

`mktemp --directory`
