# Brotli

> Compress/uncompress files with brotli compression.
> More information: <https://github.com/google/brotli>.

- Compress a file, creating a compressed version next to the file:

`brotli {{file.ext}}`

- Decompress a file, creating an uncompressed version next to the file:

`brotli -d {{file.ext}}.br`

- Compress a file specifying the output filename:

`brotli {{file.ext}} -o {{compressed_file.ext.br}}`

- Decompress a brotli file specifying the output filename:

`brotli -d {{compressed_file.ext.br}} -o {{file.ext}}`

- Specify the compression level. 1=Fastest (Worst), 11=Slowest (Best):

`brotli -q {{11}} {{file.ext}} -o {{compressed_file.ext.br}}`
