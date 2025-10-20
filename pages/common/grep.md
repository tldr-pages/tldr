# grep

> Find patterns in files using `regex`es.
> More information: <https://www.gnu.org/software/grep/manual/grep.html>.

- Search for a pattern within a file:

`grep "{{search_pattern}}" {{path/to/file1 path/to/file2 ...}}`

- Search for an exact string (disables `regex`es):

`grep {{[-F|--fixed-strings]}} "{{exact_string}}" {{path/to/file}}`

- Search for a pattern in all files recursively in a directory, showing line numbers of matches, ignoring binary files:

`grep {{[-rnI|--recursive --line-number --binary-files=without-match]}} "{{search_pattern}}" {{path/to/directory}}`

- Use extended `regex`es (supports `?`, `+`, `{}`, `()`, and `|`), in case-insensitive mode:

`grep {{[-Ei|--extended-regexp --ignore-case]}} "{{search_pattern}}" {{path/to/file}}`

- Print 3 lines of [C]ontext around, [B]efore or [A]fter each match:

`grep {{--context|--before-context|--after-context}} 3 "{{search_pattern}}" {{path/to/file}}`

- Print file name and line number for each match with color output:

`grep {{[-Hn|--with-filename --line-number]}} --color=always "{{search_pattern}}" {{path/to/file}}`

- Search for lines matching a pattern, printing only the matched text:

`grep {{[-o|--only-matching]}} "{{search_pattern}}" {{path/to/file}}`

- Search `stdin` for lines that do not match a pattern:

`cat {{path/to/file}} | grep {{[-v|--invert-match]}} "{{search_pattern}}"`
