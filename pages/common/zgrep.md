# zgrep

> Find patterns in files that may be compressed using `grep`.
> More information: <https://manned.org/zgrep>.

- Search for a pattern within a compressed file:

`zgrep "{{search_pattern}}" {{path/to/file}}`

- Search for an exact string (disables `regex`es):

`zgrep {{[-F|--fixed-strings]}} "{{exact_string}}" {{path/to/file}}`

- Print 3 lines of [C]ontext around, [B]efore, or [A]fter each match:

`zgrep {{--context=|--before-context=|--after-context=}}{{3}} "{{search_pattern}}" {{path/to/file}}`

- Print only the matched text:

`zgrep {{[-o|--only-matching]}} "{{search_pattern}}" {{path/to/file}}`

- Do not print lines that match a pattern:

`zgrep {{[-v|--invert-match]}} "{{search_pattern}}" {{path/to/file}}`

- Search for multiple patterns:

`zgrep {{[-e|--regexp]}} "{{pattern1}}" {{[-e|--regexp]}} "{{pattern2}}" {{path/to/file}}`

- Use extended `regex`es (supports `?`, `+`, `{}`, `()`, and `|`), in case-insensitive mode:

`zgrep {{[-Ei|--extended-regexp --ignore-case]}} "{{search_pattern}}" {{path/to/file}}`
