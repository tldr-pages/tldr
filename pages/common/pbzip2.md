# pbzip2

> A parallel implementation of the `bzip2` file compressor.
> See also: `bzip2`, `tar`.
> More information: <https://manned.org/pbzip2>.

- Compress a file:

`pbzip2 {{path/to/file}}`

- Compress a file using the specified number of processors:

`pbzip2 -p{{4}} {{path/to/file}}`

- Compress in combination with tar (options can be passed to `pbzip2`):

`tar -cf {{path/to/compressed_file}}.tar.bz2 {{[-I|--use-compress-program]}} "pbzip2 {{-option1 -option2 ...}}" {{path/to/file}}`

- Decompress a file:

`pbzip2 {{[-d|--decompress]}} {{path/to/compressed_file.bz2}}`

- Display help:

`pbzip2 {{[-h|--help]}}`
