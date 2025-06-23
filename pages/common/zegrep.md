# zegrep

> Find extended regular expression patterns in compressed files using `egrep`.
> More information: <https://www.unix.com/man-page/freebsd/1/zegrep/>.

- Search for extended regular expressions (supporting `?`, `+`, `{}`, `()` and `|`) in a compressed file:

`zegrep "{{search_pattern}}" {{path/to/file}}`

- Search for extended regular expressions (case-[i]nsensitive):

`zegrep -i "{{search_pattern}}" {{path/to/file}}`

- Search for lines that do not match a pattern ([v]erse the pattern):

`zegrep -v "{{search_pattern}}" {{path/to/file}}`

- Print the [H]eader (file name) and line [n]umber for each match:

`zegrep -H -n "{{search_pattern}}" {{path/to/file}}`

- Print [o]nly the matching text:

`zegrep -o "{{search_pattern}}" {{path/to/file}}`

- [r]ecursively search files in a compressed file:

`zegrep -r "{{search_pattern}}" {{path/to/file}}`
