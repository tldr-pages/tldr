# sponge

> Soak up the input before writing the output file.
> More information: <https://manned.org/sponge>.

- Append file content to the source file:

`sponge -a {{path/to/file}} < {{path/to/file}}`

- Remove all lines starting with # in a file:

`grep {{[-v|--invert-match]}} '^{{#}}' {{path/to/file}} | sponge {{path/to/file}}`
