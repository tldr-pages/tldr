# sha224sum

> Calculate SHA224 cryptographic checksums.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Calculate the SHA224 checksum for a file:

`sha224sum {{path/to/file}}`

- Calculate SHA224 checksums for multiple files:

`sha224sum {{path/to/file1}} {{path/to/file2}}`

- Calculate and save the list of SHA224 checksums to a file:

`sha224sum {{path/to/file1}} {{path/to/file2}} > {{path/to/file.sha224}}`

- Read a file of SHA224 sums and verify all files have matching checksums:

`sha224sum --check {{path/to/file.sha224}}`

- Only show a message for missing files or when verification fails:

`sha224sum --check --quiet {{path/to/file.sha224}}`

- Only show a message for files for which verification fails, ignoring missing files:

`sha224sum --ignore-missing --check --quiet {{path/to/file.sha224}}`
