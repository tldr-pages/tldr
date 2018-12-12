# zstd

> Compress or decompress files with Zstandard compression.

- Compress a file into a new file with the .zst suffix:

`zstd {{file}}`

- Decompress a file:

`zstd -d {{file}}.zstd`

- Decompress to stdout:

`zstd -dc {{file}}.zstd`

- Compress a file, while specifing the compression level. 0 = Worst, 19 = Best (Default level is 3):

`zstd -{{level}} {{file}}`

- Compress a file with high compression levels, using more memory during compression and decompression. Max level is 22:

`zstd --ultra -{{level}} {{file}}`
