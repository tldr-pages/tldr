# tac

> Print and concatenate files with lines in reversed order.
> More information: <https://www.gnu.org/software/coreutils/tac>.

- Display specific files in reversed order:

`tac {{path/to/file1 path/to/file2 ...}}`

- Display `stdin` in reversed order:

`{{cat path/to/file}} | tac`

- Use a specific [s]eparator:

`tac -s {{separator}} {{path/to/file1 path/to/file2 ...}}`

- Use a specific regex as a separator:

`tac -r -s {{separator}} {{path/to/file1 path/to/file2 ...}}`

- Use a separator before each file:

`tac -b {{path/to/file1 path/to/file2 ...}}`
