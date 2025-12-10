# zstd

> Compress or decompress files with Zstandard compression.
> More information: <https://manned.org/zstd>.

- Compress a file into a new file with the `.zst` suffix:

`zstd {{path/to/file}}`

- Decompress a file:

`zstd {{[-d|--decompress]}} {{path/to/file.zst}}`

- Decompress to `stdout`:

`zstd {{[-d|--decompress]}} {{[-c|--stdout]}} {{path/to/file.zst}}`

- Compress a file specifying the compression level, where 1=fastest, 19=slowest and 3=default:

`zstd -{{level}} {{path/to/file}}`

- Compress a file using an ultra-fast compression level, where 1=default:

`zstd --fast={{level}} {{path/to/file}}`

- Unlock higher compression levels (up to 22) using more memory (both for compression and decompression):

`zstd --ultra -{{level}} {{path/to/file}}`
