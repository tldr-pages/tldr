# lrzip

> A large file compression program.
> See also: `lrunzip`, `lrztar`, `lrzuntar`.
> More information: <https://manned.org/lrzip>.

- Compress a file with LZMA - slow compression, fast decompression:

`lrzip {{filename}}`

- Compress a file with BZIP2 - good middle ground for compression/speed:

`lrzip -b {{filename}}`

- Compress with ZPAQ - extreme compression, but very slow:

`lrzip -z {{filename}}`

- Compress with LZO - light compression, extremely fast decompression:

`lrzip -l {{filename}}`

- Compress a file and password protect/encrypt it:

`lrzip -e {{filename}}`

- Override the number of processor threads to use:

`lrzip -p {{8}} {{filename}}`
