# ptargrep

> Find regular expression patterns in tar archive files.
> More information: <https://manned.org/ptargrep>.

- Search for a pattern within a tar file:

`ptargrep "{{search_pattern}}" {{path/to/file}}`

- Search for a pattern within multiple files:

`ptargrep "{{search_pattern}}" {{path/to/file1}} {{path/to/file2}} {{path/to/file3}}`

- Extract to the current directory using the basename of the file from the archive:

`ptargrep --basename "{{search_pattern}}" {{path/to/file}}`

- Search for a case-insensitive pattern matching within a tar file:

`ptargrep --ignore-case "{{search_pattern}}" {{path/to/file}}`
