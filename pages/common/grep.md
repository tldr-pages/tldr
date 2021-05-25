# grep

> Find patterns in files using regular expressions.
> More information: <https://www.gnu.org/software/grep/manual/grep.html>.

- Search for a pattern within a file:

`grep "{{search_pattern}}" {{path/to/file}}`

- Search for an exact string (disables regular expressions):

`grep --fixed-strings "{{exact_string}}" {{path/to/file}}`

- Search for a pattern in all files recursively in a directory, showing line numbers of matches, ignoring binary files:

`grep --recursive --line-number --binary-files={{without-match}} "{{search_pattern}}" {{path/to/directory}}`

- Use extended regular expressions (supports `?`, `+`, `{}`, `()` and `|`), in case-insensitive mode:

`grep --extended-regexp --ignore-case "{{search_pattern}}" {{path/to/file}}`

- Print 3 lines of context around, before, or after each match:

`grep --{{context|before-context|after-context}}={{3}} "{{search_pattern}}" {{path/to/file}}`

- Print file name and line number for each match:

`grep --with-filename --line-number "{{search_pattern}}" {{path/to/file}}`

- Search for lines matching a pattern, printing only the matched text:

`grep --only-matching "{{search_pattern}}" {{path/to/file}}`

- Search stdin for lines that do not match a pattern:

`cat {{path/to/file}} | grep --invert-match "{{search_pattern}}"`
