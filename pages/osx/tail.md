# tail

> Display the last part of a file.
> See also: `head`.
> More information: <https://manned.org/man/freebsd-13.0/tail.1>.

- Show last 'count' lines in file:

`tail -n {{count}} {{path/to/file}}`

- Print a file from a specific line number:

`tail -n +{{count}} {{path/to/file}}`

- Print a specific count of bytes from the end of a given file:

`tail -c {{count}} {{path/to/file}}`

- Print the last lines of a given file and keep reading file until `Ctrl + C`:

`tail -f {{path/to/file}}`

- Keep reading file until `Ctrl + C`, even if the file is inaccessible:

`tail -F {{path/to/file}}`

- Show last 'count' lines in 'file' and refresh every 'seconds' seconds:

`tail -n {{count}} -s {{seconds}} -f {{path/to/file}}`
