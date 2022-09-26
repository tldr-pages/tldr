# hexdump

> An ASCII, decimal, hexadecimal, octal dump.
> More information: <https://manned.org/hexdump>.

- Print the hexadecimal representation of a file, replacing duplicate lines by '*':

`hexdump {{file}}`

- Display the input offset in hexadecimal and its ASCII representation in two columns:

`hexdump -C {{file}}`

- Display the hexadecimal representation of a file, but interpret only n bytes of the input:

`hexdump -C -n{{number_of_bytes}} {{file}}`

- Don't replace duplicate lines with '*':

`hexdump --no-squeezing {{file}}`
