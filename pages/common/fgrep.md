# fgrep

> Matches patterns in files.
> Supports simple patterns and regular expressions.
> More information: <https://manned.org/fgrep>.

- Search for an exact string in a file:

`fgrep {{search_string}} {{path/to/file}}`

- Search only lines that match entirely in files:

`fgrep -x {{path/to/file1}} {{path/to/file2}}`

- Count the number of lines that match the given string in a file:

`fgrep -c {{search_string}} {{path/to/file}}`

- Show the line number in the file along with the line matched:

`fgrep -n {{search_string}} {{path/to/file}}`

- Display all lines except those that contain the given regular expression:

`fgrep -v {{^regex$}} {{path/to/file}}`

- Display filenames whose content matches the regular expression at least once:

`fgrep -l {{^regex$}} {{path/to/file1}} {{path/to/file2}}`
