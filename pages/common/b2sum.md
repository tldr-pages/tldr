# b2sum

> Calculate BLAKE2 cryptographic checksums.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/b2sum-invocation.html>.

- Calculate the BLAKE2 checksum for one or more files:

`b2sum {{path/to/file1 path/to/file2 ...}}`

- Calculate and save the list of BLAKE2 checksums to a file:

`b2sum {{path/to/file1 path/to/file2 ...}} > {{path/to/file.b2}}`

- Calculate a BLAKE2 checksum from `stdin`:

`{{command}} | b2sum`

- Read a file of BLAKE2 checksums and filenames and verify all files have matching checksums:

`b2sum {{[-c|--check]}} {{path/to/file.b2}}`

- Only show a message for missing files or when verification fails:

`b2sum {{[-c|--check]}} --quiet {{path/to/file.b2}}`

- Only show a message when verification fails, ignoring missing files:

`b2sum --ignore-missing {{[-c|--check]}} --quiet {{path/to/file.b2}}`

- Check a known BLAKE2 checksum of a file:

`echo {{known_blake2_checksum_of_the_file}} {{path/to/file}} | b2sum {{[-c|--check]}}`
