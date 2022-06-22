# ugrep

> Ultra fast search tool with query TUI.
> More information: <https://github.com/Genivia/ugrep>.

- Start a query TUI to search files in the current directory recursively (CTRL-Z for help):

`ugrep --query`

- Search the current directory recursively for files containing a regex search pattern:

`ugrep "{{search_pattern}}"`

- Search a specific file or search all files in the specified directory, showing line numbers of matches:

`ugrep --line-number "{{search_pattern}}" {{path/to/file_or_directory}}`

- List the matching files in the current directory recursively:

`ugrep --files-with-matches "{{search_pattern}}"`

- Fuzzy search files with up to 3 extra, missing or mismatching characters in the pattern:

`ugrep --fuzzy=3 "{{search_pattern}}"`

- Search compressed files, zip and tar archives recursively:

`ugrep --decompress "{{search_pattern}}"`

- Search only files whose filenames match a specific glob pattern:

`ugrep --glob="{{foo*.???}}" "{{search_pattern}}"`

- Search only C++ source files (use `--type=list` to list all file types):

`ugrep --type=cpp "{{search_pattern}}"`
