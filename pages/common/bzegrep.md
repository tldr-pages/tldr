# bzegrep

> Find extended regular expression patterns in `bzip2` compressed files using `egrep`.
> More information: <https://manned.org/bzegrep>.

- Search for extended regular expressions (supporting `?`, `+`, `{}`, `()` and `|`) in a compressed file (case-sensitive):

`bzegrep "{{search_pattern}}" {{path/to/file}}`

- Search for extended regular expressions (supporting `?`, `+`, `{}`, `()` and `|`) in a compressed file (case-insensitive):

`bzegrep --ignore-case "{{search_pattern}}" {{path/to/file}}`

- Search for lines that do not match a pattern:

`bzegrep --invert-match "{{search_pattern}}" {{path/to/file}}`

- Print file name and line number for each match:

`bzegrep --with-filename --line-number "{{search_pattern}}" {{path/to/file}}`

- Search for lines matching a pattern, printing only the matched text:

`bzegrep --only-matching "{{search_pattern}}" {{path/to/file}}`

- Recursively search files in a `bzip2` compressed `tar` archive for a pattern:

`bzegrep --recursive "{{search_pattern}}" {{path/to/file}}`
