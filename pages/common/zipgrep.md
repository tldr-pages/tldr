# zipgrep

> Find patterns in files in a Zip archive using extended `regex` (supports `?`, `+`, `{}`, `()`, and `|`).
> More information: <https://manned.org/zipgrep>.

- Search for a pattern within a Zip archive:

`zipgrep "{{search_pattern}}" {{path/to/file.zip}}`

- Print file name and line number for each match:

`zipgrep {{[-H|--with-filename]}} {{[-n|--line-number]}} "{{search_pattern}}" {{path/to/file.zip}}`

- Search for lines that do not match a pattern:

`zipgrep {{[-v|--invert-match]}} "{{search_pattern}}" {{path/to/file.zip}}`

- Include only specific files inside a Zip archive in the search:

`zipgrep "{{search_pattern}}" {{path/to/file.zip}} {{path/to/included_file1 path/to/included_file2 ...}}`

- Exclude files inside a Zip archive from search:

`zipgrep "{{search_pattern}}" {{path/to/file.zip}} -x {{path/to/excluded_file1 path/to/excluded_file2 ...}}`
