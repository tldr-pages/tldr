# gzip

> Compress/uncompress files with gzip compression (LZ77)

- compress a file, replacing it with a gzipped compressed version

`gzip {{file.ext}}`

- decompress a file, replacing it with the original uncompressed version

`gzip -d {{file.ext.gz}}`

- compress a file specifying the output filename

`gzip -c {{file.ext}} > compressed-file.ext.gz`

- uncompress a gzipped file specifying the output filename

`gzip -c -d {{file.ext.gz}} > uncompressed-file.ext`

- specify the compression level. 1=Fastest (Worst), 9=Slowest (Best), Default level is 6

`gzip -9 -c {{file.ext}} > compressed-file.ext.gz`
