# b2sum

> Calculate BLAKE2 cryptographic checksums.
> More information: <https://www.gnu.org/software/coreutils/b2sum>.

- Calculate the BLAKE2 checksum for a file:

`b2sum {{path/to/file}}`

- Calculate BLAKE2 checksums for multiple files:

`b2sum {{path/to/file1}} {{path/to/file2}}`

- Read a file of BLAKE2 sums and filenames and verify all files have matching checksums:

`b2sum -c {{path/to/file.b2}}`

- Calculate the BLAKE2 checksum from stdin:

`{{some_command}} | b2sum`
