# b3sum

> Calculate BLAKE3 cryptographic checksums.
> More information: <https://github.com/BLAKE3-team/BLAKE3/tree/master/b3sum>.

- Calculate the BLAKE3 checksum for one or more files:

`b3sum {{path/to/file1 path/to/file2 ...}}`

- Calculate and save the list of BLAKE3 checksums to a file:

`b3sum {{path/to/file1 path/to/file2 ...}} > {{path/to/file.b3}}`

- Calculate a BLAKE3 checksum from `stdin`:

`{{command}} | b3sum`

- Read a file of BLAKE3 sums and filenames and verify all files have matching checksums:

`b3sum --check {{path/to/file.b3}}`

- Only show a message for missing files or when verification fails:

`b3sum --check --quiet {{path/to/file.b3}}`
