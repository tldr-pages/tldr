# tail

> Display the last part of a file.
> See also: `head`.
> More information: <https://www.gnu.org/software/coreutils/tail>.

- Show last 'count' lines in file:

`tail --lines {{count}} {{path/to/file}}`

- Print a file from a specific line number:

`tail --lines +{{count}} {{path/to/file}}`

- Print a specific count of bytes from the end of a given file:

`tail --bytes {{count}} {{path/to/file}}`

- Print the last lines of a given file and keep reading file until `Ctrl + C`:

`tail --follow {{path/to/file}}`

- Keep reading file until `Ctrl + C`, even if the file is inaccessible:

`tail --retry --follow {{path/to/file}}`

- Show last 'num' lines in 'file' and refresh every 'n' seconds:

`tail --lines {{count}} --sleep-interval {{seconds}} --follow {{path/to/file}}`
