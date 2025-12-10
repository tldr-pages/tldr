# lrzip

> A large file compression program.
> See also: `lrunzip`, `lrztar`, `lrzuntar`.
> More information: <https://manned.org/lrzip>.

- Compress a file with LZMA - slow compression, fast decompression:

`lrzip {{path/to/file}}`

- Compress a file with BZIP2 - good middle ground for compression/speed:

`lrzip {{[-b|--bzip2]}} {{path/to/file}}`

- Compress with ZPAQ - extreme compression, but very slow:

`lrzip {{[-z|--zpaq]}} {{path/to/file}}`

- Compress with LZO - light compression, extremely fast decompression:

`lrzip {{[-l|--lzo]}} {{path/to/file}}`

- Compress a file and password protect/encrypt it:

`lrzip {{[-e|--encrypt]}} {{path/to/file}}`

- Override the number of processor threads to use:

`lrzip {{[-p|--threads]}} {{8}} {{path/to/file}}`
