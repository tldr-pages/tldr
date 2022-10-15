# xzcat

> Data compression tool similar to `gzip` and `bzip2` syntax.
> Compresses or decompresses `.xz` and `.lzma` files.
> More information: <https://manned.org/xzcat>.

- Compress a file then delete it:

`xzcat --compress {{path/to/file}}`

- Decompress a specific archive then delete it:

`xzcat --decompress {{path/to/archive.xz}}`

- Test the integrity of a specific archive:

`xzcat --test {{path/to/archive.xz}}`

- List the contents of a specific archive:

`xzcat --list {{path/to/file}}`

- Compress a file without delete it:

`xzcat --keep {{path/to/file}}`

- Compress a file overwriting the output archive compressing the target of symbolic links:

`xzcat --force {{path/to/file}}`

- Compress a file suppressing warnings (use two `--quiet` flags to suppress errors too):

`xzcat --quiet {{path/to/file}}`
