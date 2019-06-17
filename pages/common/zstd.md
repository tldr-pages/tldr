# zstd

> Compress or decompress files with Zstandard compression.
> More information: <https://github.com/facebook/zstd>.

- Compress a file into a new file with the .zst suffix:

`zstd {{file}}`

- Decompress a file:

`zstd -d {{file}}.zst`

- Decompress to `stdout`:

`zstd -dc {{file}}.zst`

- Compress a file, while specifing the compression level. 0 = Worst, 19 = Best (Default level is 3):

`zstd -{{level}} {{file}}`

- Use more memory (both when compressing and decompressing) to achieve a higher compression ratio:

`zstd --ultra -{{level}} {{file}}`
