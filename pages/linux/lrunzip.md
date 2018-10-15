# lrunzip

> A large file decompression program. See also `lrzip`, `lrztar`, `lrzuntar`.

- Decompress a file:

`lrunzip {{filename.lrz}}`

- Decompress a file with more processor threads:

`lrunzip -p {{8}} {{filename.lrz}}`

- Decompress a file, silently overwriting files if they exist:

`lrunzip -f {{filename.lrz}}`
