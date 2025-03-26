# help2man

> Produce simple man pages from an executable's `--help` and `--version` output.
> More information: <https://www.gnu.org/software/help2man>.

- Generate a man page for an executable:

`help2man {{executable}}`

- Specify the "name" paragraph in the man page:

`help2man {{executable}} {{[-n|--name]}} {{name}}`

- Specify the section for the man page (defaults to 1):

`help2man {{executable}} {{[-s|--section]}} {{section}}`

- Output to a file instead of `stdout`:

`help2man {{executable}} {{[-o|--output]}} {{path/to/file}}`

- Display help:

`help2man --help`
