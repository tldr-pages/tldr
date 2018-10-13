# lrzip

> A large file compression program.

- Compress a directory with LZMA compression:

`lrztar {{directory}}`

- Decompress a directory that used the above:

`lrzuntar {{directory.tar.lrz}}`

- Compress a file with LZMA - slow compression, fast decompression:

`lrzip {{filename}}`

- Compress with ZPAQ - extreme compression, but slow:

`lrzip -z {{filename}}`

- Compress with LZO - light compression, extremely fast decompression:

`lrzip -l {{filename}}`

- Decompress archive to file:

`lrunzip {{filename.lrz}}`
