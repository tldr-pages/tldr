# tail

> Display the last part of a file.
> See also: `head`.
> More information: <https://manned.org/man/freebsd-13.0/tail.1>.

- Show last 'count' lines in file:

`tail -n {{count}} {{path/to/file}}`

- Show all file since line 'count':

`tail -n +{{count}} {{path/to/file}}`

- Show last 'count' bytes in file:

`tail -c {{count}} {{path/to/file}}`

- Keep reading file until `Ctrl + C`:

`tail -f {{path/to/file}}`

- Keep reading file until `Ctrl + C`, even if the file is inaccessible:

`tail -F {{path/to/file}}`

- Show last 'count' lines in 'file' and refresh every 'seconds' seconds:

`tail -n {{count}} -s {{seconds}} -f {{path/to/file}}`
