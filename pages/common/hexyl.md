# hexyl

> A simple hex viewer for the terminal. Uses colored output to distinguish different categories of bytes.
> More information: <https://github.com/sharkdp/hexyl>.

- Print the hexadecimal representation of a file:

`hexyl {{file}}`

- Print the hexadecimal representation of a file, but interpret only n bytes of the input:

`hexyl -n {{bytes_to_read}} {{file}}`

- Print bytes N through M of a file:

`hexyl -r {{N}}:{{M}} {{file}}`

- Print 512 bytes starting at the 1024th byte:

`hexyl -r 1024:+512 {{file}}`
