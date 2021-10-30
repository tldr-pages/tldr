# cmp

> Compare two files byte by byte.
> More information: <https://www.gnu.org/software/diffutils/manual/html_node/Invoking-cmp.html>.

- Find the byte and line number of the first difference between two files:

`cmp {{path/to/file1}} {{path/to/file2}}`

- Find the byte number and differing bytes of every difference:

`cmp -l {{path/to/file1}} {{path/to/file2}}`
