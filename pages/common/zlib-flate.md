# zlib-flate

> Raw zlib compression and decompression program.
> Part of `qpdf`.
> More information: <https://manned.org/zlib-flate>.

- Compress a file:

`zlib-flate -compress < {{path/to/input_file}} > {{path/to/compressed.zlib}}`

- Uncompress a file:

`zlib-flate -uncompress < {{path/to/compressed.zlib}} > {{path/to/output_file}}`

- Compress a file with a specified compression level. 0=Fastest (Worst), 9=Slowest (Best):

`zlib-flate -compress={{compression_level}} < {{path/to/input_file}} > {{path/to/compressed.zlib}}`
