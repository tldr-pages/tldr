# od

> Display file contents in octal, decimal or hexadecimal format.
> Optionally display the byte offsets and/or printable representation for each line.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/od-invocation.html>.

- Display file using default settings: octal format, 8 bytes per line, byte offsets in octal, and duplicate lines replaced with `*`:

`od {{path/to/file}}`

- Display file in verbose mode, i.e. without replacing duplicate lines with `*`:

`od {{[-v|--output-duplicates]}} {{path/to/file}}`

- Display file in hexadecimal format (2-byte units), with byte offsets in decimal format:

`od {{[-t|--format]}} {{x}} {{[-A|--address-radix]}} {{d}} {{[-v|--output-duplicates]}} {{path/to/file}}`

- Display file in hexadecimal format (1-byte units), and 4 bytes per line:

`od {{[-t|--format]}} {{x1}} {{[-w|--width=]}}4 {{[-v|--output-duplicates]}} {{path/to/file}}`

- Display file in hexadecimal format along with its character representation, and do not print byte offsets:

`od {{[-t|--format]}} {{xz}} {{[-A|--address-radix]}} {{n}} {{[-v|--output-duplicates]}} {{path/to/file}}`

- Read only 100 bytes of a file starting from the 500th byte:

`od {{[-N|--read-bytes]}} 100 {{[-j|--skip-bytes]}} 500 {{[-v|--output-duplicates]}} {{path/to/file}}`
