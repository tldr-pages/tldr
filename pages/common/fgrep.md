# fgrep

> Matches fixed strings in files.
> Equivalent to `grep -F`.
> More information: <https://www.gnu.org/software/grep/manual/grep.html>.

- Search for an exact string in a file:

`fgrep {{search_string}} {{path/to/file}}`

- Search only lines that match entirely in files:

`fgrep -x {{path/to/file1}} {{path/to/file2}}`

- Count the number of lines that match the given string in a file:

`fgrep -c {{search_string}} {{path/to/file}}`

- Show the line number in the file along with the line matched:

`fgrep -n {{search_string}} {{path/to/file}}`

- Display all lines except those that contain the search string:

`fgrep -v {{search_string}} {{path/to/file}}`

- Display filenames whose content matches the search string at least once:

`fgrep -l {{search_string}} {{path/to/file1}} {{path/to/file2}}`
