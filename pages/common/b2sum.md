# b2sum

> Calculate BLAKE2 cryptographic checksums.
> More information: <https://www.gnu.org/software/coreutils/b2sum>.

- Calculate the BLAKE2 checksum for one or more files:

`b2sum {{path/to/file1 path/to/file2 ...}}`

- Calculate and save the list of BLAKE2 checksums to a file:

`b2sum {{path/to/file1 path/to/file2 ...}} > {{path/to/file.b2}}`

- Calculate a BLAKE2 checksum from `stdin`:

`{{command}} | b2sum`

- Read a file of BLAKE2 sums and filenames and verify all files have matching checksums:

`b2sum --check {{path/to/file.b2}}`

- Only show a message for missing files or when verification fails:

`b2sum --check --quiet {{path/to/file.b2}}`

- Only show a message when verification fails, ignoring missing files:

`b2sum --ignore-missing --check --quiet {{path/to/file.b2}}`
