# fgrep

> Matches patterns in files.
> Supports simple patterns and regular expressions.

- Search for an exact string in a file:

`fgrep {{search_string}} {{path/to/file}}`

- Search only lines that match entirely in files: 

`fgrep -x {{path/to/file1}} {{path/to/file2}}`

-Count of number of lines that match the given string in a file:

`fgrep -c {{search_string}} {{path/to/file}}`

- Shows line number of file with the line matched:

`fgrep -n {{search_string}} {{path/to/file}}`

- Display all lines except those that contain the regular expression:

`fgrep -v {{^regex$}} {{path/to/file}}`

- Search the file names that match the regular expression:

`fgrep -l {{^regex$}} {{path/to/file1}} {{path/to/file2}}`
