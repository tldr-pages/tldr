# xz

> Compress or decompress XZ and LZMA files.
> More information: <https://manned.org/xz>.

- Compress a file using xz:

`xz {{path/to/file}}`

- Decompress an XZ file:

`xz --decompress {{path/to/file.xz}}`

- Compress a file using lzma:

`xz --format=lzma {{path/to/file}}`

- Decompress an LZMA file:

`xz --decompress --format=lzma {{path/to/file.lzma}}`

- Decompress a file and write to `stdout` (implies `--keep`):

`xz --decompress --stdout {{path/to/file.xz}}`

- Compress a file, but don't delete the original:

`xz --keep {{path/to/file}}`

- Compress a file using the fastest compression:

`xz -0 {{path/to/file}}`

- Compress a file using the best compression:

`xz -9 {{path/to/file}}`
