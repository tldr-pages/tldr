# colordiff

> A tool to colorize diff output.
> The Perl script colordiff is a wrapper for `diff` and produces the same output but with pretty syntax highlighting. Color schemes can be customized.
> More information: <https://github.com/kimmel/colordiff>.

- Compare files:

`colordiff {{path/to/file1}} {{path/to/file2}}`

- Output in two columns:

`colordiff -y {{path/to/file1}} {{path/to/file2}}`

- Ignore case differences in file contents:

`colordiff -i {{path/to/file1}} {{path/to/file2}}`

- Report when two files are the same:

`colordiff -s {{path/to/file1}} {{path/to/file2}}`

- Ignore white spaces:

`colordiff -w {{path/to/file1}} {{path/to/file2}}`
