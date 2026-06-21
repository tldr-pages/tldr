# bzgrep

> Find patterns in `bzip2` compressed files using `grep`.
> More information: <https://manned.org/bzgrep>.

- Search for a pattern within a compressed file:

`bzgrep "{{search_pattern}}" {{path/to/file}}`

- Search for an exact string (disables `regex`es):

`bzgrep -F "{{exact_string}}" {{path/to/file}}`

- Print 3 lines of [C]ontext around, [B]efore, or [A]fter each match:

`bzgrep {{-C|-B|-A}}{{3}} "{{search_pattern}}" {{path/to/file}}`

- Print the line number for each match:

`bzgrep -n "{{search_pattern}}" {{path/to/file}}`

- Print only the matched text:

`bzgrep -o "{{search_pattern}}" {{path/to/file}}`

- Do not print lines that match a pattern:

`bzgrep -v "{{search_pattern}}" {{path/to/file}}`

- Use extended `regex`es (supports `?`, `+`, `{}`, `()`, and `|`), in case-insensitive mode:

`bzgrep -Ei "{{search_pattern}}" {{path/to/file}}`
