# colordiff

> A wrapper around `diff` that produces the same output but with pretty syntax highlighting.
> Color schemes can be customized.
> More information: <https://github.com/kimmel/colordiff>.

- Compare files:

`colordiff {{file1}} {{file2}}`

- Output in two columns:

`colordiff -y {{file1}} {{file2}}`

- Ignore case differences in file contents:

`colordiff -i {{file1}} {{file2}}`

- Report when two files are the same:

`colordiff -s {{file1}} {{file2}}`

- Ignore whitespace:

`colordiff -w {{file1}} {{file2}}`
