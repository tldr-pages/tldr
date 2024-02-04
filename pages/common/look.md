# look

> Display lines beginning with a prefix in a sorted file.
> NOTE: the lines in the file must be sorted.
> See also: `grep`, `sort`.
> More information: <https://man.openbsd.org/look>.

- Search for lines beginning with a specific prefix in a specific file:

`look {{prefix}} {{path/to/file}}`

- Case-insensitively ([f]) search only on alphanumeric characters ([d]):

`look -f -d {{prefix}} {{path/to/file}}`

- Specify a string [t]ermination character (space by default):

`look -t {{,}}`

- Search in `/usr/share/dict/words` (`-d` and `-f` are assumed):

`look {{prefix}}`
