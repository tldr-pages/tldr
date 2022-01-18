# wc

> Count lines, words, or bytes.
> Get help or version: wc --help|--version.
> More information: <https://www.gnu.org/software/coreutils/wc>.

- Count lines in file:

`wc --lines {{path/to/file}}`

- Count words in file:

`wc --words {{path/to/file}}`

- Count characters (bytes) in file:

`wc --bytes {{path/to/file}}`

- Count characters in file (taking multi-byte character sets into account):

`wc --chars {{path/to/file}}`

- Use standard input to count lines, words and characters (bytes) in that order:

`{{find .}} | wc`
