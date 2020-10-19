# hexyl

> A simple hex viewer for the terminal. Uses colored output to distinguish different categories of bytes.
> More information: <https://github.com/sharkdp/hexyl>.

- Print the hexadecimal representation of a file:

`hexyl {{path/to/file}}`

- Print the hexadecimal representation of the first n bytes of a file:

`hexyl -n {{n}} {{path/to/file}}`

- Print bytes 512 through 1024 of a file:

`hexyl -r {{512}}:{{1024}} {{path/to/file}}`

- Print 512 bytes starting at the 1024th byte:

`hexyl -r {{1024}}:+{{512}} {{path/to/file}}`
