# grep

> Matches patterns in input text.
> Supports simple patterns and regular expressions.

- Search for an exact string:

`grep {{something}} {{file_path}}`

- Search in case-insensitive mode:

`grep -i {{something}} {{path/to/file}}`

- Search recursively in current directory for an exact string:

`grep -r {{something}} .`

- Use a regular expression (`-E` for extended regex, supporting `?`, `+`, `{}`, `()` and `|`):

`grep -e {{^regex$}} {{path/to/file}}`

- Print 3 lines of context around each match:

`grep -C 3 {{something}} {{path/to/file}}`

- Print the count of matches instead of the matching text:

`grep -c {{something}} {{path/to/file}}`

- Print line number for each match:

`grep -n {{something}} {{path/to/file}}`

- Print file names with matches:

`grep -rl {{something}} .`

- Use the standard input instead of a file:

`cat {{path/to/file}} | grep {{something}}`

- Invert match for excluding specific strings:

`grep -v {{something}}`
