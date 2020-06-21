# zstd

> Compress or decompress files with Zstandard compression.
> More information: <https://github.com/facebook/zstd>.

- Compress a file into a new file with the .zst suffix:

`zstd {{file}}`

- Decompress a file:

`zstd -d {{file}}.zst`

- Decompress to `stdout`:

`zstd -dc {{file}}.zst`

- Compress a file, while specifing the compression level (1=Fastest, 19=Strongest, 3=Default):

`zstd -{{level}} {{file}}`

- Unlock higher compression levels (up to 22) using more memory (both for compression and decompression):

`zstd --ultra -{{level}} {{file}}`
