# lrunzip

> A large file decompression program.
> See also `lrzip`, `lrztar`, `lrzuntar`.
> More information: <https://manned.org/lrunzip>.

- Decompress a file:

`lrunzip {{path/to/file.lrz}}`

- Decompress a file using a specific number of processor threads:

`lrunzip -p {{8}} {{path/to/file.lrz}}`

- Decompress a file and silently overwrite files if they exist:

`lrunzip -f {{path/to/file.lrz}}`

- Keep broken or damaged files instead of deleting them when decompressing:

`lrunzip -K {{path/to/file.lrz}}`

- Specify output file name and/or path:

`lrunzip -o {{outfilename}} {{path/to/file.lrz}}`
