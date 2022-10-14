# xzcat

> Data compression tool similar to `gzip` and `bzip2` syntax.
> Compresses or decompresses `.xz` and `.lzma` files.
> More information: <https://manned.org/xzcat>.

- Force compress:

`xzcat --compress {{path/to/file}}`

- Decompress a file:

`xzcat --decopress {{path/to/file.xz}}`

- Test the integrity of a specific archive:

`xzcat --test {{path/to/archive.xz}}`

- List the contents of a specific archive:

`xzcat --list {{path/to/file}}`

- Compress a file without delete it:

`xzcat --keep {{path/to/file}}`

- Force overwrite output files and decompress links:

`xzcat --force {{path/to/file}}`

- Suppress warnings (Specify twice to suppress warning and errors):

`xzcat --quiet {{path/to/file}}`
