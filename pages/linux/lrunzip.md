# lrunzip

> A large file decompression program.
> See also: `lrzip`, `lrztar`, `lrzuntar`.
> More information: <https://manned.org/lrunzip>.

- Decompress a file:

`lrunzip {{filename.lrz}}`

- Decompress a file using a specific number of processor threads:

`lrunzip -p {{8}} {{filename.lrz}}`

- Decompress a file and silently overwrite files if they exist:

`lrunzip -f {{filename.lrz}}`

- Keep broken or damaged files instead of deleting them when decompressing:

`lrunzip -K {{filename.lrz}}`

- Specify output file name and/or path:

`lrunzip -o {{outfilename}} {{filename.lrz}}`
