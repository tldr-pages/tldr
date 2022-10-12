# hexdump

> Display file contents in hexadecimal, decimal, octal, or ascii.
> More information: <https://man7.org/linux/man-pages/man1/hexdump.1.html>.

- Display the input offset in hexadecimal, followed by three columns of data in octal, per line:

`hexdump -b {{path/to/file}}`

- Display the input offset in hexadecimal, followed by same sixteen bytes in `%_p` format enclosed in `|` characters:

`hexdump --canonical {{path/to/file}}`

- Interpret only specified length bytes of the input:

`hexdump --length {{7}} {{path/to/file}}`

- Skip offset bytes from the beginning of the input and interpret:

`hexdump --skip {{5}} {{path/to/file}}`

- Display all data in hexadecimal without skipping any output lines:

`hexdump -v {{path/to/file}}`
