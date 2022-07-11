# tac

> Display and concatenate files with lines in reversed order.
> See also: `cat`.
> More information: <https://www.gnu.org/software/coreutils/tac>.

- Concatenate specific files in reversed order:

`tac {{path/to/file1 path/to/file2 ...}}`

- Display `stdin` in reversed order:

`{{cat path/to/file}} | tac`

- Use a specific [s]eparator:

`tac -s {{separator}} {{path/to/file1 path/to/file2 ...}}`

- Use a specific [r]egex as a [s]eparator:

`tac -r -s {{separator}} {{path/to/file1 path/to/file2 ...}}`

- Use a separator [b]efore each file:

`tac -b {{path/to/file1 path/to/file2 ...}}`
