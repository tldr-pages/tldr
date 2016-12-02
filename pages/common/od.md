# od

> Display file contents in hexadecimal, octal, or printable character format.
> Optionally display the byte offsets into the file.

- Display file in octal format 8 bytes per line with the byte offsets in octal as well replacing duplicate lines with '*':

`od {{/path/to/file}}`

- Display file in hexadecimal format with byte offsets in hexadecimal, 4 bytes per line with each entry 1 byte long:

`od --address-radix=x --format=x1 --width=4 -v {{/path/to/file}}`

- Display only printable strings of at least 5 characters long in the file along with the byte offsets in hexadecimal:

`od --address-radix=x --string=5 -v {{/path/to/file}}`

- Read only given number of first bytes of a file and display it in the hexadecimal format:

`od --address-radix=x --format=x --read-bytes 100 -v {{/path/to/file}}`

- Display file in hexadecimal format along with its character representation, also do not print byte offsets:

`od --address-radix=n --format=xz -v {{/path/to/file}}`

