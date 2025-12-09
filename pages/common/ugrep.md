# ugrep

> Ultra fast search tool with query TUI.
> More information: <https://github.com/Genivia/ugrep#man-page>.

- Start a query TUI to search files in the current directory recursively (`<Ctrl z>` for help):

`ugrep {{[-Q|--query]}}`

- Search the current directory recursively for files containing a `regex` search pattern:

`ugrep "{{search_pattern}}"`

- Search in a specific file or in all files in a specific directory, showing line numbers of matches:

`ugrep {{[-n|--line-number]}} "{{search_pattern}}" {{path/to/file_or_directory}}`

- Search in all files in the current directory recursively and print the name of each matching file:

`ugrep {{[-l|--files-with-matches]}} "{{search_pattern}}"`

- Fuzzy search files with up to 3 extra, missing or mismatching characters in the pattern:

`ugrep {{[-Z|--fuzzy=]}}{{3}} "{{search_pattern}}"`

- Also search compressed files, Zip and tar archives recursively:

`ugrep {{[-z|--decompress]}} "{{search_pattern}}"`

- Search only files whose filenames match a specific glob pattern:

`ugrep {{[-g |--glob=]}}"{{glob_pattern}}" "{{search_pattern}}"`

- Search only C++ source files (use `--file-type=list` to list all file types):

`ugrep {{[-t |--file-type=]}}cpp "{{search_pattern}}"`
