# tail

> Display the last part of a file.
> See also: `head`.
> More information: <https://keith.github.io/tail.1.html>.

- Show last 'count' lines in file:

`tail -n {{8}} {{path/to/file}}`

- Print a file from a specific line number:

`tail -n +{{8}} {{path/to/file}}`

- Print a specific count of bytes from the end of a given file:

`tail -c {{8}} {{path/to/file}}`

- Print the last lines of a given file and keep reading it until `Ctrl + C`:

`tail -f {{path/to/file}}`

- Keep reading file until `Ctrl + C`, even if the file is inaccessible:

`tail -F {{path/to/file}}`

- Show last 'count' lines in 'file' and refresh every 'seconds' seconds:

`tail -n {{8}} -s {{10}} -f {{path/to/file}}`
