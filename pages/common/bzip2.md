# bzip2

> A block-sorting file compressor.
> More information: <https://manned.org/bzip2>.

- Compress a file:

`bzip2 {{path/to/file_to_compress}}`

- Decompress a file:

`bzip2 -d {{path/to/compressed_file.bz2}}`

- Decompress a file to standard output:

`bzip2 -dc {{path/to/compressed_file.bz2}}`

- Test compressed file integrity:

`bzip2 -t {{path/to/compressed_file.bz2}}`

- Show the compression ratio for each file processed in [v]erbose mode:

`bzip2 -v {{path/to/compressed_files.bz2}}`

- Overwrite existing output files:

`bzip2 -f {{path/to/compressed_file.bz2}}`

- Print help:

`bzip2 -h`
