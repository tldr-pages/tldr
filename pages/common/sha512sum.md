# sha512sum

> Calculate SHA512 cryptographic checksums.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Calculate the SHA512 checksum for a file:

`sha512sum {{path/to/file}}`

- Calculate SHA512 checksums for multiple files:

`sha512sum {{path/to/file1}} {{path/to/file2}}`

- Calculate and save the list of SHA512 checksums to a file:

`sha512sum {{path/to/file1}} {{path/to/file2}} > {{path/to/file.sha512}}`

- Read a file of SHA512 sums and verify all files have matching checksums:

`sha512sum --check {{path/to/file.sha512}}`

- Only show a message for missing files or when verification fails:

`sha512sum --check --quiet {{path/to/file.sha512}}`

- Only show a message for files for which verification fails, ignoring missing files:

`sha512sum --ignore-missing --check --quiet {{path/to/file.sha512}}`
