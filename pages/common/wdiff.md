# wdiff

> Display word differences between text files.
> More information: <https://www.gnu.org/software/wdiff/manual/html_node/wdiff-invocation.html#wdiff-invocation>.

- Compare two files:

`wdiff {{path/to/file1}} {{path/to/file2}}`

- Ignore case when comparing:

`wdiff {{[-i|--ignore-case]}} {{path/to/file1}} {{path/to/file2}}`

- Display how many words are deleted, inserted or replaced:

`wdiff {{[-s|--statistics]}} {{path/to/file1}} {{path/to/file2}}`
