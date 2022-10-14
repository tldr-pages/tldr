# xzcat

> A general purpose data compression tool similar to gzip and bzip2 syntaxes.
> Compresses or decompresses .xz and .lzma files.
> More information: <https://www.unix.com/man-page/linux/1/xzcat/>.

- Force compress:

`xzcat --compress {{path/to/file}}`

- Force decompress:

`xzcat --decopress {{path/to/file}}`

- Test compressed file integrity:

`xzcat --test {{path/to/file}}`

- List information about .xz file:

`xzcat --list {{path/to/file}}`

- Keep/Avoid deleting input files:

`xzcat --keep {{path/to/file}}`

- Force overwrite output files and decompress links:

`xzcat --force {{path/to/file}}`

- Suppress warnings (Specify twice to suppress warning and errors):

`xzcat --quiet {{path/to/file}}`
