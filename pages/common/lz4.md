# lz4

> Compress or decompress .lz4 files.
> More information: <https://github.com/lz4/lz4>.

- Compress a file:

`lz4 {{file}}`

- Decompress a file:

`lz4 -d {{file.lz4}}`

- Decompress a file and write to stdout:

`lz4 -dc {{file.lz4}}`

- Package and compress a directory and its contents:

`tar cvf - {{path/to/dir}} | lz4 - {{dir.tar.lz4}}`

- Decompress and unpack a directory and its contents:

`lz4 -d {{dir.tar.lz4}} | tar -xv`

- Compress a file using the best compression:

`lz4 -9 {{file}}`
