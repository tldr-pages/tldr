# xz

> Compress or decompress XZ and LZMA files.
> More information: <https://manned.org/xz>.

- Compress a file using xz:

`xz {{path/to/file}}`

- Decompress an XZ file:

`xz {{[-d|--decompress]}} {{path/to/file.xz}}`

- Compress a file using lzma:

`xz {{[-F|--format]}} lzma {{path/to/file}}`

- Decompress an LZMA file:

`xz {{[-d|--decompress]}} {{[-F|--format]}} lzma {{path/to/file.lzma}}`

- Decompress a file and write to `stdout` (implies `--keep`):

`xz {{[-d|--decompress]}} {{[-c|--stdout]}} {{path/to/file.xz}}`

- Compress a file, but don't delete the original:

`xz {{[-k|--keep]}} {{path/to/file}}`

- Compress a file using the fastest compression:

`xz -0 {{path/to/file}}`

- Compress a file using the best compression:

`xz -9 {{path/to/file}}`
