# zegrep

> Find extended regular expression patterns in compressed files using `egrep`.
> More information: <https://www.unix.com/man-page/freebsd/1/zegrep/>.

- Search for extended regular expressions (supporting `?`, `+`, `{}`, `()` and `|`) in a compressed file (case-sensitive):

`zegrep "{{search_pattern}}" {{path/to/file}}`

- Search for extended regular expressions (supporting `?`, `+`, `{}`, `()` and `|`) in a compressed file (case-insensitive):

`zegrep --ignore-case "{{search_pattern}}" {{path/to/file}}`

- Search for lines that do not match a pattern:

`zegrep --invert-match "{{search_pattern}}" {{path/to/file}}`

- Print file name and line number for each match:

`zegrep --with-filename --line-number "{{search_pattern}}" {{path/to/file}}`

- Search for lines matching a pattern, printing only the matched text:

`zegrep --only-matching "{{search_pattern}}" {{path/to/file}}`

- Recursively search files in a compressed file for a pattern:

`zegrep --recursive "{{search_pattern}}" {{path/to/file}}`
