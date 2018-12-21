# xz

> Compress or decompress .xz and .lzma files.

- Compress a file:

`xz {{file}}`

- Decompress a file:

`xz -d {{file.xz}}`

- Decompress a file and write to stdout:

`xz -dc {{file.xz}}`

- Compress a file, but don't delete the original:

`xz -k {{file}}`

- Compress a file using the fastest compression:

`xz -0 {{file}}`

- Compress a file using the best compression:

`xz -9 {{file}}`
