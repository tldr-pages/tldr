# grep

> Matches patterns in input text.
> Supports simple patterns and regular expressions.

- Search for a pattern within a file:

`grep {{search_pattern}} {{path/to/file}}`

- Search for an exact string:

`grep -F {{exact_string}} {{path/to/file}}`

- Search for a pattern recursively in the current directory, ignoring non-text files:

`grep -RI {{search_pattern}} .`

- Use extended regular expressions (supporting `?`, `+`, `{}`, `()` and `|`), in case-insensitive mode:

`grep -Ei {{search_pattern}} {{path/to/file}}`

- Print 3 lines of [C]ontext around, [B]efore, or [A]fter each match:

`grep -{{C|B|A}} 3 {{search_pattern}} {{path/to/file}}`

- Print file name with the corresponding line number for each match:

`grep -Hn {{search_pattern}} {{path/to/file}}`

- Use the standard input instead of a file:

`cat {{path/to/file}} | grep {{search_pattern}}`

- Invert match for excluding specific strings:

`grep -v {{search_pattern}}`
