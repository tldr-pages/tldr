# grep

> Matches patterns in input text.
> Supports simple patterns and regular expressions.

- Search for an exact string:

`grep {{search_string}} {{path/to/file}}`

- Search in case-insensitive mode:

`grep -i {{search_string}} {{path/to/file}}`

- Search recursively (ignoring non-text files) in current directory for an exact string:

`grep -RI {{search_string}} .`

- Use extended regular expressions (supporting `?`, `+`, `{}`, `()` and `|`):

`grep -E {{^regex$}} {{path/to/file}}`

- Print 3 lines of [C]ontext around, [B]efore, or [A]fter each match:

`grep -{{C|B|A}} 3 {{search_string}} {{path/to/file}}`

- Print file name with the corresponding line number for each match:

`grep -Hn {{search_string}} {{path/to/file}}`

- Use the standard input instead of a file:

`cat {{path/to/file}} | grep {{search_string}}`

- Invert match for excluding specific strings:

`grep -v {{search_string}}`
