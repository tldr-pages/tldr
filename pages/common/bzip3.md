# bzip3

> An efficient statistical file compressor.
> More information: <https://manned.org/bzip3>.

- Compress a file:

`bzip3 {{path/to/file_to_compress}}`

- Decompress a file:

`bzip3 {{[-d|--decode]}} {{path/to/compressed_file.bz3}}`

- Decompress a file to `stdout`:

`bzip3 {{[-dc|--decode --stdout]}} {{path/to/compressed_file.bz3}}`

- Test the integrity of each file inside the archive file:

`bzip3 {{[-t|--test]}} {{path/to/compressed_file.bz3}}`

- Show the compression ratio for each file processed with detailed information:

`bzip3 {{[-v|--verbose]}} {{path/to/compressed_files.bz3}}`

- Decompress a file overwriting existing files:

`bzip3 {{[-d|--decode]}} {{[-f--force]}} {{path/to/compressed_file.bz3}}`

- Display help:

`bzip3 {{[-h|--help]}}`
