# gzip

> Compress/uncompress files with `gzip` compression (LZ77).
> More information: <https://www.gnu.org/software/gzip/manual/gzip.html>.

- Compress a file, replacing it with a `gzip` archive:

`gzip {{file.ext}}`

- Decompress a file, replacing it with the original uncompressed version:

`gzip -d {{file.ext}}.gz`

- Compress a file, keeping the original file:

`gzip --keep {{file.ext}}`

- Compress a file specifying the output filename:

`gzip -c {{file.ext}} > {{compressed_file.ext.gz}}`

- Decompress a `gzip` archive specifying the output filename:

`gzip -c -d {{file.ext}}.gz > {{uncompressed_file.ext}}`

- Specify the compression level. 1=Fastest (Worst), 9=Slowest (Best), Default level is 6:

`gzip -9 -c {{file.ext}} > {{compressed_file.ext.gz}}`
