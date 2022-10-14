# xzcat

> A general purpose data compression tool similar to gzip and bzip2 syntaxes.
> Compress or decompress .xz and .lzma files.
> More information: <https://www.unix.com/man-page/linux/1/xzcat/>.

- Force compress:

`xzcat --compress {{path/to/file}}`

- Force decompress:

`xzcat --decompress {{path/to/file}}`

- Test compressed file integrity:

`xzcat --test {{path/to/file}}`

- List information about the .xz file:

`xzcat --list {{path/to/file}}`

- Keep/Avoid deleting input files:

`xzcat --keep {{path/to/file}}`

- Force overwrite output files and decompress links:

`xzcat --force {{path/to/file}}`

- Extreme compression using more CPU time:

`xzcat --extreme {{path/to/file}}`

- Supress Warnings. (Specify twice to supress warnings and errors):

`xzcat --quiet {{path/to/file}}`
