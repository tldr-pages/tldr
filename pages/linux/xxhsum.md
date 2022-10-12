# xxhsum

> Print or verify checksums using fast non-cryptographic algorithm xxHash.
> More information: <https://github.com/Cyan4973/xxHash>.

- Calculate the checksum for a file using a specific algorithm:

`xxhsum -H{{0|32|64|128}} {{path/to/file}}`

- Run benchmark:

`xxhsum -b`
