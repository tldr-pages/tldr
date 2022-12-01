# paste

> Merge lines of files.
> More information: <https://www.gnu.org/software/coreutils/paste>.

- Join all the lines into a single line, using TAB as delimiter:

`paste -s {{path/to/file}}`

- Join all the lines into a single line, using the specified delimiter:

`paste -s -d {{delimiter}} {{path/to/file}}`

- Merge two files side by side, each in its column, using TAB as delimiter:

`paste {{path/to/file1}} {{path/to/file2}}`

- Merge two files side by side, each in its column, using the specified delimiter:

`paste -d {{delimiter}} {{path/to/file1}} {{path/to/file2}}`

- Merge two files, with lines added alternatively:

`paste -d '\n' {{path/to/file1}} {{path/to/file2}}`
