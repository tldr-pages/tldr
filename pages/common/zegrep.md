# zegrep

> Find extended `regex` patterns in compressed files using `egrep`.
> More information: <https://www.unix.com/man-page/freebsd/1/zegrep/>.

- Search for extended `regex` (supporting `?`, `+`, `{}`, `()` and `|`) in a compressed file (case-sensitive):

`zegrep "{{search_pattern}}" {{path/to/file}}`

- Search for extended `regex` (supporting `?`, `+`, `{}`, `()` and `|`) in a compressed file (case-insensitive):

`zegrep {{[-i|--ignore-case]}} "{{search_pattern}}" {{path/to/file}}`

- Search for lines that do not match a pattern:

`zegrep {{[-v|--invert-match]}} "{{search_pattern}}" {{path/to/file}}`

- Print file name and line number for each match:

`zegrep {{[-H|--with-filename]}} {{[-n|--line-number]}} "{{search_pattern}}" {{path/to/file}}`

- Search for lines matching a pattern, printing only the matched text:

`zegrep {{[-o|--only-matching]}} "{{search_pattern}}" {{path/to/file}}`

- Recursively search files in a compressed file for a pattern:

`zegrep {{[-r|--recursive]}} "{{search_pattern}}" {{path/to/file}}`
