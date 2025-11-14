# difftastic

> A structural diff tool that compares files based on their syntax.
> More information: <https://difftastic.wilfred.me.uk>.

- Compare two files:

`difft {{path/to/file1}} {{path/to/file2}}`

- Compare files and display output in side-by-side mode:

`difft {{[-d|--display]}} side-by-side {{path/to/file1}} {{path/to/file2}}`

- Compare files and display output inline:

`difft {{[-d|--display]}} inline {{path/to/file1}} {{path/to/file2}}`

- Compare files with a specific tab width:

`difft {{[--tab-width]}} {{4}} {{path/to/file1}} {{path/to/file2}}`

- Compare files and ignore whitespace changes:

`difft {{[--ignore-whitespace]}} {{path/to/file1}} {{path/to/file2}}`

- Compare files with specific language syntax highlighting:

`difft {{[--language]}} {{javascript}} {{path/to/file1}} {{path/to/file2}}`

- Compare files and show only a summary:

`difft {{[--summary]}} {{path/to/file1}} {{path/to/file2}}`

- Display help:

`difft {{[-h|--help]}}`