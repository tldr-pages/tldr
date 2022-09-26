# wc

> Count lines, words, and bytes.
> More information: <https://www.gnu.org/software/coreutils/wc>.

- Count all lines in a file:

`wc --lines {{path/to/file}}`

- Count all words in a file:

`wc --words {{path/to/file}}`

- Count all bytes in a file:

`wc --bytes {{path/to/file}}`

- Count all characters in a file (taking multi-byte characters into account):

`wc --chars {{path/to/file}}`

- Count all lines, words and bytes from `stdin`:

`{{find .}} | wc`

- Count the length of the longest line in number of characters:

`wc --max-line-length {{path/to/file}}`
