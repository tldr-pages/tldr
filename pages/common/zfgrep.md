# zfgrep

> Matches fixed strings in possibly compressed files.
> Equivalent to `grep --fixed-strings` with input decompressed first if necessary.
> More information: <https://manned.org/zfgrep>.

- Search for an exact string in a file:

`zfgrep {{search_string}} {{path/to/file}}`

- Count the number of lines that match the given string in a file:

`zfgrep {{[-c|--count]}} {{search_string}} {{path/to/file}}`

- Show the line number in the file along with the matching lines:

`zfgrep {{[-n|--line-number]}} {{search_string}} {{path/to/file}}`

- Display all lines except those that contain the search string:

`zfgrep {{[-v|--invert-match]}} {{search_string}} {{path/to/file}}`

- List only filenames whose content matches the search string at least once:

`zfgrep {{[-l|--files-with-matches]}} {{search_string}} {{path/to/file1 path/to/file2 ...}}`
