# bat

> Print and concatenate files.
> A `cat` clone with syntax highlighting and Git integration.
> More information: <https://github.com/sharkdp/bat>.

- Pretty print the contents of one or more files to `stdout`:

`bat {{path/to/file1 path/to/file2 ...}}`

- Concatenate several files into the target file:

`bat {{path/to/file1 path/to/file2 ...}} > {{path/to/target_file}}`

- Remove decorations and disable paging (`--style plain` can be replaced with `-p`, or both options with `-pp`):

`bat --style plain --pager never {{path/to/file}}`

- Highlight a specific line or a range of lines with a different background color:

`bat {{--highlight-line|-H}} {{10|5:10|:10|10:|10:+5}} {{path/to/file}}`

- Show non-printable characters like space, tab or newline:

`bat {{--show-all|-A}} {{path/to/file}}`

- Remove all decorations except line numbers in the output:

`bat {{--number|-n}} {{path/to/file}}`

- Syntax highlight a JSON file by explicitly setting the language:

`bat {{--language|-l}} json {{path/to/file.json}}`

- Display all supported languages:

`bat {{--list-languages|-L}}`
