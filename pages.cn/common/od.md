# od

> Display file contents in octal, decimal or hexadecimal format.
> Optionally display the byte offsets and/or printable representation for each line.

- Display file using default settings: octal format, 8 bytes per line, byte offsets in octal, and duplicate lines replaced with `*`:

`od {{path/to/file}}`

- Display file in verbose mode, i.e. without replacing duplicate lines with `*`:

`od -v {{path/to/file}}`

- Display file in hexadecimal format (2-byte units), with byte offsets in decimal format:

`od --format={{x}} --address-radix={{d}} -v {{path/to/file}}`

- Display file in hexadecimal format (1-byte units), and 4 bytes per line:

`od --format={{x1}} --width={{4}} -v {{path/to/file}}`

- Display file in hexadecimal format along with its character representation, and do not print byte offsets:

`od --format={{xz}} --address-radix={{n}} -v {{path/to/file}}`

- Read only 100 bytes of a file starting from the 500th byte:

`od --read-bytes {{100}} --skip-bytes={{500}} -v {{path/to/file}}`
