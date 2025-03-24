# wc

> Count lines, words, and bytes.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/wc-invocation.html>.

- Count all lines in a file:

`wc {{[-l|--lines]}} {{path/to/file}}`

- Count all words in a file:

`wc {{[-w|--words]}} {{path/to/file}}`

- Count all bytes in a file:

`wc {{[-c|--bytes]}} {{path/to/file}}`

- Count all characters in a file (taking multi-byte characters into account):

`wc {{[-m|--chars]}} {{path/to/file}}`

- Count all lines, words and bytes from `stdin`:

`{{find .}} | wc`

- Count the length of the longest line in number of characters:

`wc {{[-L|--max-line-length]}} {{path/to/file}}`
