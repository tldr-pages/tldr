# bzip2

> A block-sorting file compressor.
> More information: <https://manned.org/bzip2>.

- Compress a file:

`bzip2 {{path/to/file_to_compress}}`

- Decompress a file:

`bzip2 {{[-d|--decompress]}} {{path/to/compressed_file.bz2}}`

- Decompress a file to `stdout`:

`bzip2 {{[-dc|--decompress --stdout]}} {{path/to/compressed_file.bz2}}`

- Test the integrity of each file inside the archive file:

`bzip2 {{[-t|--test]}} {{path/to/compressed_file.bz2}}`

- Show the compression ratio for each file processed with detailed information:

`bzip2 {{[-v|--verbose]}} {{path/to/compressed_files.bz2}}`

- Decompress a file overwriting existing files:

`bzip2 {{[-f|--force]}} {{path/to/compressed_file.bz2}}`

- Display help:

`bzip2 {{[-h|--help]}}`
