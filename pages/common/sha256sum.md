# sha256sum

> Calculate SHA256 cryptographic checksums.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Calculate the SHA256 checksum for a file:

`sha256sum {{path/to/file}}`

- Calculate SHA256 checksums for multiple files:

`sha256sum {{path/to/file1}} {{path/to/file2}}`

- Calculate and save the list of SHA256 checksums to a file:

`sha256sum {{path/to/file1}} {{path/to/file2}} > {{path/to/file.sha256}}`

- Read a file of SHA256 sums and verify all files have matching checksums:

`sha256sum --check {{path/to/file.sha256}}`

- Only show a message for missing files or when verification fails:

`sha256sum --check --quiet {{path/to/file.sha256}}`

- Only show a message for files for which verification fails, ignoring missing files:

`sha256sum --ignore-missing --check --quiet {{path/to/file.sha256}}`
