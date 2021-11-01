# wc

> Count lines, words, or bytes.
> More information: <https://www.gnu.org/software/coreutils/wc>.

- Count lines in file:

`wc -l {{file}}`

- Count words in file:

`wc -w {{file}}`

- Count characters (bytes) in file:

`wc -c {{file}}`

- Count characters in file (taking multi-byte character sets into account):

`wc -m {{file}}`

- Use standard input to count lines, words and characters (bytes) in that order:

`{{find .}} | wc`
