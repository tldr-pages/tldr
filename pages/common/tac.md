# tac

> Display and concatenate files with lines in reversed order.
> See also: `cat`.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/tac-invocation.html>.

- Concatenate specific files in reversed order:

`tac {{path/to/file1 path/to/file2 ...}}`

- Display `stdin` in reversed order:

`{{cat path/to/file}} | tac`

- Use a specific separator:

`tac {{[-s|--separator]}} {{separator}} {{path/to/file1 path/to/file2 ...}}`

- Use a specific `regex` as a separator:

`tac {{[-r|--regex]}} {{[-s|--separator]}} {{separator}} {{path/to/file1 path/to/file2 ...}}`

- Use a separator before each file:

`tac {{[-b|--before]}} {{path/to/file1 path/to/file2 ...}}`
