# grep

> Find patterns in files using `regex`es.
> See also: `regex`.
> More information: <https://www.gnu.org/software/grep/manual/grep.html>.

- Search for a pattern within files:

`grep "{{search_pattern}}" {{path/to/file1 path/to/file2 ...}}`

- Search for an exact string (disables `regex`es):

`grep {{[-F|--fixed-strings]}} "{{exact_string}}" {{path/to/file}}`

- Search for a pattern in all files recursively in a directory, ignoring binary files:

`grep {{[-rI|--recursive --binary-files=without-match]}} "{{search_pattern}}" {{path/to/directory}}`

- Print 3 lines of [C]ontext around, [B]efore, or [A]fter each match:

`grep {{--context|--before-context|--after-context}} 3 "{{search_pattern}}" {{path/to/file}}`

- Print file name and line number for each match with color output:

`grep {{[-Hn|--with-filename --line-number]}} --color=always "{{search_pattern}}" {{path/to/file}}`

- Print only the matched text:

`grep {{[-o|--only-matching]}} "{{search_pattern}}" {{path/to/file}}`

- Read data from `stdin` and do not print lines that match a pattern:

`cat {{path/to/file}} | grep {{[-v|--invert-match]}} "{{search_pattern}}"`

- Use extended `regex`es (supports `?`, `+`, `{}`, `()`, and `|`), in case-insensitive mode:

`grep {{[-Ei|--extended-regexp --ignore-case]}} "{{search_pattern}}" {{path/to/file}}`
