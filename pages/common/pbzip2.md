# pbzip2

> A parallel implementation of the `bzip2` file compressor.
> See also: `bzip2`, `tar`.
> More information: <https://manned.org/pbzip2>.

- Compress a file:

`pbzip2 {{path/to/file}}`

- Compress a file using the specified number of processors:

`pbzip2 -p{{4}} {{path/to/file}}`

- [d]ecompress a file:

`pbzip2 --decompress {{path/to/compressed_file.bz2}}`

- Display help:

`pbzip2 -h`
