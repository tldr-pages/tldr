# paste

> Merge lines of files.

- join all the lines into a single line, using TAB as delimiter.

`paste -s {{file}}`

- join all the lines into a single line, using the specified delimiter.

`paste -s -d {{delimiter}} {{file}}`

- merge two files side by side, each in its column, using TAB as delimiter.

`paste {{file1}} {{file2}}`

- merge two files side by side, each in its column, using the specified delimiter.

`paste -d {{delimiter}} {{file1}} {{file2}}`

- merge two files, with lines added alternatively.

`paste -d '\n' {{file1}} {{file2}}`
