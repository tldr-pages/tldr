# zlib-flate

> Raw zlib compression and decompression program.
> The zlib-flate program is part of the qpdf package.
> More information: <https://manned.org/zlib-flate>.

- Compress a file:

`zlib-flate -compress < {{path/to/input_file}} > {{path/to/compressed.zlib}}`

- Uncompress a file:

`zlib-flate -uncompress < {{compressed.zlib}} > {{file}}`

- Compress a file with a specified compression level [0-9]:

`zlib-flate -compress={{compression_level}} < {{path/to/input_file}} > {{path/to/compressed.zlib}}`
