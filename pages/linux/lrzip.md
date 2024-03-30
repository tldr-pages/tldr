# lrzip

> A large file compression program.
> See also: `lrunzip`, `lrztar`, `lrzuntar`.
> More information: <https://manned.org/lrzip>.

- Compress a file with LZMA - slow compression, fast decompression:

`lrzip {{path/to/file}}`

- Compress a file with BZIP2 - good middle ground for compression/speed:

`lrzip -b {{path/to/file}}`

- Compress with ZPAQ - extreme compression, but very slow:

`lrzip -z {{path/to/file}}`

- Compress with LZO - light compression, extremely fast decompression:

`lrzip -l {{path/to/file}}`

- Compress a file and password protect/encrypt it:

`lrzip -e {{path/to/file}}`

- Override the number of processor threads to use:

`lrzip -p {{8}} {{path/to/file}}`
