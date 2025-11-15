# zlib-flate

> Raw zlib compression and decompression program.
> Part of `qpdf`.
> More information: <https://manned.org/zlib-flate>.

- Compress a file:

`zlib-flate < {{path/to/input_file}} -compress > {{path/to/compressed.zlib}}`

- Uncompress a file:

`zlib-flate < {{path/to/compressed.zlib}} -uncompress > {{path/to/output_file}}`

- Compress a file with a specified compression level. 0=Fastest (Worst), 9=Slowest (Best):

`zlib-flate < {{path/to/input_file}} -compress={{compression_level}} > {{path/to/compressed.zlib}}`
