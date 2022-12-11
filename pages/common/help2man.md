# help2man

> Produce simple man pages from an executable's `--help` and `--version` output.
> More information: <https://www.gnu.org/software/help2man>.

- Generate a man page for an executable:

`help2man {{executable}}`

- Specify the "name" paragraph in the man page:

`help2man {{executable}} --name {{name}}`

- Specify the section for the man page (defaults to 1):

`help2man {{executable}} --section {{section}}`

- Output to a file instead of `stdout`:

`help2man {{executable}} --output {{path/to/file}}`

- Display detailed help:

`help2man --help`
