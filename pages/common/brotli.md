# brotli

> Compress/uncompress files with Brotli compression.
> More information: <https://github.com/google/brotli>.

- Compress a file, creating a compressed version next to the file:

`brotli {{path/to/file.ext}}`

- Decompress a file, creating an uncompressed version next to the file:

`brotli -d {{path/to/file.ext.br}}`

- Compress a file specifying the output filename:

`brotli {{path/to/file.ext}} -o {{path/to/compressed_output_file.ext.br}}`

- Decompress a Brotli file specifying the output filename:

`brotli -d {{path/to/compressed_file.ext.br}} -o {{path/to/output_file.ext}}`

- Specify the compression level [1=Fastest (Worst), 11=Slowest (Best)]:

`brotli -q {{11}} {{path/to/file.ext}} -o {{path/to/compressed_output_file.ext.br}}`
