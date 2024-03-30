# brotli

> Compress/uncompress files with Brotli compression.
> More information: <https://github.com/google/brotli>.

- Compress a file, creating a compressed version next to the file:

`brotli {{path/to/file}}`

- [d]ecompress a file, creating an uncompressed version next to the file:

`brotli -d {{path/to/file.br}}`

- Compress a file specifying the [o]utput filename:

`brotli {{path/to/file}} -o {{path/to/compressed_output_file.br}}`

- [d]ecompress a Brotli file specifying the [o]utput filename:

`brotli -d {{path/to/compressed_file.br}} -o {{path/to/output_file}}`

- Specify the compression quality (1=fastest (worst), 11=slowest (best)):

`brotli -q {{11}} {{path/to/file}} -o {{path/to/compressed_output_file.br}}`
