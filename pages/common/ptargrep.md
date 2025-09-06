# ptargrep

> Find `regex` patterns in tar archive files.
> More information: <https://manned.org/ptargrep>.

- Search for a pattern within one or more tar archives:

`ptargrep "{{search_pattern}}" {{path/to/file1 path/to/file2 ...}}`

- Extract to the current directory using the basename of the file from the archive:

`ptargrep {{[-b|--basename]}} "{{search_pattern}}" {{path/to/file}}`

- Search for a case-insensitive pattern matching within a tar archive:

`ptargrep {{[-i|--ignore-case]}} "{{search_pattern}}" {{path/to/file}}`
