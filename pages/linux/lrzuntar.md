# lrzuntar

> A wrapper for `lrunzip` to simplify decompression of directories.
> See also: `lrztar`, `lrzip`.

- Decompress from file to a directory:

`lrzuntar {{path/to/directory.tar.lrz}}`

- Decompress from file to a directory using a specific number of processor threads:

`lrzuntar -p {{8}} {{path/to/directory.tar.lrz}}`

- Decompress from file to a directory and silently overwrite items that already exist:

`lrzuntar -f {{directory.tar.lrz}}`

- Specify output path:

`lrzuntar -O {{path/to/directory}} {{directory.tar.lrz}}`

- Delete compressed file after decompressing to directory:

`lrzuntar -D {{path/to/directory.tar.lrz}}`
