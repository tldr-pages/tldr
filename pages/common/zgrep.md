# zgrep

> Grep text patterns from files within compressed file (equivalent to `grep -Z`).
> More information: <https://manned.org/zgrep>.

- Grep a pattern in a compressed file (case-sensitive):

`zgrep {{pattern}} {{path/to/compressed/file}}`

- Grep a pattern in a compressed file (case-insensitive):

`zgrep {{[-i|--ignore-case]}} {{pattern}} {{path/to/compressed/file}}`

- Output count of lines containing matched pattern in a compressed file:

`zgrep {{[-c|--count]}} {{pattern}} {{path/to/compressed/file}}`

- Display the lines which don’t have the pattern present (Invert the search function):

`zgrep {{[-v|--invert-match]}} {{pattern}} {{path/to/compressed/file}}`

- Grep a compressed file for multiple patterns:

`zgrep {{[-e|--regexp]}} "{{pattern_1}}" {{[-e|--regexp]}} "{{pattern_2}}" {{path/to/compressed/file}}`

- Use extended regular expressions (supporting `?`, `+`, `{}`, `()` and `|`):

`zgrep {{[-E|--extended-regexp]}} {{regular_expression}} {{path/to/file}}`

- Print 3 lines of [C]ontext around, [B]efore, or [A]fter each match:

`zgrep --{{context|before-context|after-context}} 3 {{pattern}} {{path/to/compressed/file}}`
