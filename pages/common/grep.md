# grep

> Matches patterns in input text.
> Supports simple patterns and regular expressions.
> More information: <https://man7.org/linux/man-pages/man1/grep.1.html>.

- Search for a pattern within a file:

`grep {{search_pattern}} {{path/to/file}}`

- Search for an exact ([F]ixed) string:

`grep -F {{exact_string}} {{path/to/file}}`

- Search for a pattern [R]ecursively in the current directory, showing matching line [n]umbers, [I]gnoring non-text files:

`grep -RIn {{search_pattern}} {{.}}`

- Use [E]xtended regular expressions (supporting `?`, `+`, `{}`, `()` and `|`), in case-[i]nsensitive mode:

`grep -Ei {{search_pattern}} {{path/to/file}}`

- Print 3 lines of [C]ontext around, [B]efore, or [A]fter each match:

`grep -{{C|B|A}} {{3}} {{search_pattern}} {{path/to/file}}`

- Print file name [H]eaders with the corresponding line [n]umber for each match:

`grep -Hn {{search_pattern}} {{path/to/file}}`

- Search for lines matching a pattern, printing [o]nly the matched text:

`grep -o {{search_pattern}} {{path/to/file}}`

- Search for lines that do not match (in[v]ert) a pattern:

`grep -v {{search_pattern}}`
