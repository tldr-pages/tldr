# bat

> Print and concatenate files.
> A `cat` clone with syntax highlighting and Git integration.
> More information: <https://github.com/sharkdp/bat>.

- Pretty print the contents of one or more files to `stdout`:

`bat {{path/to/file1 path/to/file2 ...}}`

- Concatenate several files into the target file:

`bat {{path/to/file1 path/to/file2 ...}} > {{path/to/target_file}}`

- Remove decorations and auto paging:

`bat --style=plain --pager=never {{path/to/file}}`

- Highlight specific line or range of lines with different background color:

`bat --highlight-line {{10|5:10|:10|10:|10:+5}} {{path/to/file}}`

- Show non-printable characters like space, tab or newline:

`bat --show-all {{path/to/file}}`

- Remove decorations except line numbers in output:

`bat --number {{path/to/file}}`

- Syntax highlight a JSON file by explicitly setting the language:

`bat --language json {{path/to/file.json}}`

- Display all supported languages:

`bat --list-languages`
