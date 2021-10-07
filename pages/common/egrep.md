# egrep

> Find patterns in files using extended regular expression (supports `?`, `+`, `{}`, `()` and `|`).
> More information: <https://manned.org/egrep>.

- Search for a pattern within a file:

`egrep "{{search_pattern}}" {{path/to/file}}`

- Search for a pattern within multiple files:

`egrep "{{search_pattern}}" {{path/to/file1}} {{path/to/file2}} {{path/to/file3}}`

- Search stdin for a pattern:

`cat {{path/to/file}} | egrep {{search_pattern}}`

- Print file name and line number for each match:

`egrep --with-filename --line-number "{{search_pattern}}" {{path/to/file}}`

- Search for a pattern in all files recursively in a directory, ignoring binary files:

`egrep --recursive --binary-files={{without-match}} "{{search_pattern}}" {{path/to/directory}}`

- Search for lines that do not match a pattern:

`egrep --invert-match "{{search_pattern}}" {{path/to/file}}`
