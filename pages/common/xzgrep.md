# xzgrep

> Search files possibly compressed with `xz`, `lzma`, `gzip`, `bzip2`, `lzop`, or `zstd` using regular expressions.
> See also: `grep`.
> More information: <https://manned.org/xzgrep>.

- Search for a pattern within a file:

`xzgrep "{{search_pattern}}" {{path/to/file}}`

- Search for an exact string (disables regular expressions):

`xzgrep {{[-F|--fixed-strings]}} "{{exact_string}}" {{path/to/file}}`

- Search for a pattern in all files showing line numbers of matches:

`xzgrep {{[-n|--line-number]}} "{{search_pattern}}" {{path/to/file}}`

- Use extended regular expressions (supports `?`, `+`, `{}`, `()` and `|`), in case-insensitive mode:

`xzgrep {{[-E|--extended-regexp]}} {{[-i|--ignore-case]}} "{{search_pattern}}" {{path/to/file}}`

- Print 3 lines of [C]ontext around, [B]efore, or [A]fter each match:

`xzgrep --{{context|before-context|after-context}} {{3}} "{{search_pattern}}" {{path/to/file}}`

- Print file name and line number for each match with color output:

`xzgrep {{[-H|--with-filename]}} {{[-n|--line-number]}} --color=always "{{search_pattern}}" {{path/to/file}}`

- Search for lines matching a pattern, printing only the matched text:

`xzgrep {{[-o|--only-matching]}} "{{search_pattern}}" {{path/to/file}}`
