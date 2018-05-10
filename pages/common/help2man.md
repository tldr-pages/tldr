# help2man

> Produce simple man pages from an executable's `--help` and `--version` output.

- Generate a man page for an executable:

`help2man {{executable}}`

- Specify the "name" paragraph in the man page:

`help2man {{executable}} --name {{name}}`

- Specify the section for the man page (defaults to 1):

`help2man {{executable}} --section {{section}}`

- Specify the source, or footer, of the man page:

`help2man {{executable}} --source {{source}}`

- Specify a custom `--version` option for the executable:

`help2man {{executable}} --version-string {{version}}`

- Include additional information from a file if it exists:

`help2man {{executable}} --opt-include {{path/to/file}}`

- Output to a file instead of stdout:

`help2man {{executable}} --output {{path/to/file}}`

- Display detailed help:

`help2man --help`
