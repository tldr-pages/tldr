# gzip

> Compress/uncompress files with gzip compression (LZ77).
> More information: <https://www.gnu.org/software/gzip/manual/gzip.html>.

- Compress a file, replacing it with a gzipped compressed version:

`gzip {{path/to/file.ext}}`

- Decompress a file, replacing it with the original uncompressed version:

`gzip -d {{path/to/file.ext}}.gz`

- Compress a file, keeping the original file:

`gzip --keep {{path/to/file.ext}}`

- Compress a file specifying the output filename:

`gzip -c {{path/to/file.ext}} > {{path/to/file.gz}}`

- Decompress a gzipped file specifying the output filename:

`gzip -c -d {{path/to/file.ext}}.gz > {{path/to/file.ext}}`

- Specify the compression level. 1=Fastest (Worst), 9=Slowest (Best), Default level is 6:

`gzip -9 -c {{path/to/file.ext}} > {{path/to/file.gz}}`
