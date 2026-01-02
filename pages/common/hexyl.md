# hexyl

> A simple hex viewer for the terminal. Uses colored output to distinguish different categories of bytes.
> See also: `od`, `xxd`, `hexdump`.
> More information: <https://github.com/sharkdp/hexyl/blob/master/doc/hexyl.1.md>.

- Print the hexadecimal representation of a file:

`hexyl {{path/to/file}}`

- Print the hexadecimal representation of the first n bytes of a file:

`hexyl {{[-n|--length]}} {{n}} {{path/to/file}}`
