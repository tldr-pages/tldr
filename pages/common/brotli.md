# brotli

> Compress/uncompress files with Brotli compression.
> More information: <https://github.com/google/brotli>.

- Compress a file, creating a compressed version next to the file:

`brotli {{path/to/file}}`

- Decompress a file, creating an uncompressed version next to the file:

`brotli -d {{path/to/file.br}}`

- Compress a file specifying the output filename:

`brotli {{path/to/file}} -o {{path/to/compressed_output_file.br}}`

- Decompress a Brotli file specifying the output filename:

`brotli -d {{path/to/compressed_file.br}} -o {{path/to/output_file}}`

- Specify the compression level [1=Fastest (Worst), 11=Slowest (Best)]:

`brotli -q {{11}} {{path/to/file}} -o {{path/to/compressed_output_file.br}}`
