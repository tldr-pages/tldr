# look

> Display lines beginning with a prefix in a sorted file.
> See also: `grep`, `sort`.
> More information: <https://man.freebsd.org/cgi/man.cgi?look>.

- Search for lines beginning with a specific prefix in a specific file:

`look {{prefix}} {{path/to/file}}`

- Case-insensitively search only on alphanumeric characters:

`look {{-f|--ignore-case}} {{-d|--alphanum}} {{prefix}} {{path/to/file}}`

- Specify a string termination character (space by default):

`look {{-t|--terminate}} {{,}}`

- Search in `/usr/share/dict/words` (`--ignore-case` and `--alphanum` are assumed):

`look {{prefix}}`
