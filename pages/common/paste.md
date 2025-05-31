# paste

> Merge lines of files.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/paste-invocation.html>.

- Join all the lines into a single line, using TAB as delimiter:

`paste {{[-s|--serial]}} {{path/to/file}}`

- Join all the lines into a single line, using the specified delimiter:

`paste {{[-sd|--serial --delimiters]}} {{delimiter}} {{path/to/file}}`

- Merge two files side by side, each in its column, using TAB as delimiter:

`paste {{path/to/file1}} {{path/to/file2}}`

- Merge two files side by side, each in its column, using the specified delimiter:

`paste {{[-d|--delimiters]}} {{delimiter}} {{path/to/file1}} {{path/to/file2}}`

- Merge two files, with lines added alternatively:

`paste {{[-d|--delimiters]}} '\n' {{path/to/file1}} {{path/to/file2}}`
