# lzgrep

> Search compressed files using the `grep` utility.
> More information: <https://manned.org/lzgrep>.

- Search for a pattern in a compressed file:

`lzgrep "{{search_pattern}}" {{file.lzma}}`

- Search in a compressed file [r]ecursively:

`lzgrep -r "{{search_pattern}}" {{path/to/directory}}/*.lzma`

- Search in a compressed file and display the line [n]umber:

`lzgrep -n "{{search_pattern}}" {{file.lzma}}`

- Search in a compressed file and display the filename:

`lzgrep -H "{{search_pattern}}" {{file.lzma}}`

- Search in a compressed file and display the [c]ontext:

`lzgrep -C {{number_of_lines}} "{{search_pattern}}" {{file.lzma}}`
