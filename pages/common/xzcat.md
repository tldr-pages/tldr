# xzcat

> Data compression tool similar to `gzip` and `bzip2` syntax.
> Compresses or decompresses `.xz` and `.lzma` files.
> More information: <https://manned.org/xzcat>.

- Force compress:

`xzcat --compress {{path/to/file}}`

- Force decompress:

`xzcat --decopress {{path/to/file}}`

- Test compressed file integrity:

`xzcat --test {{path/to/file}}`

- List the contents of a specific archive:

`xzcat --list {{path/to/file}}`

- Compress a file without delete it:

`xzcat --keep {{path/to/file}}`

- Force overwrite output files and decompress links:

`xzcat --force {{path/to/file}}`

- Suppress warnings (Specify twice to suppress warning and errors):

`xzcat --quiet {{path/to/file}}`
