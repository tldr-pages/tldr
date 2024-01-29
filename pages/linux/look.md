# look

> Display lines in a beginning with a prefix.
> NOTE: the lines in the file must be sorted.
> See also: `grep`, `sort`.
> More information: <https://manned.org/look>.

- Search for lines beginning with a specific prefix in a specific file:

`look {{prefix}} {{path/to/file}}`

- Case-insensitively search only on blank and alphanumeric characters:

`look -{{f|-ignore-case}} -{{d|-alphanum}} {{prefix}} {{path/to/file}}`

- Specify a string termination character (space by default):

`look --terminate ,`

- Search in `/usr/share/dict/words` (`--ignore-case` and `--alphanum` are assumed):

`look {{prefix}}`

- Search in `/usr/share/dict/web2` (`--ignore-case` and `--alphanum` are assumed):

`look --alternative {{prefix}}`
