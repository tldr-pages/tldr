# sha256sum

> Calculate SHA256 cryptographic checksums.

- Calculate the SHA256 checksum for a file:

`sha256sum {{filename1}}`

- Calculate SHA256 checksums for multiple files:

`sha256sum {{filename1}} {{filename2}}`

- Calculate and save the list of SHA256 checksums to a file:

`sha256sum {{filename1}} {{filename2}} > {{filename.sha256}}`

- Read a file of SHA256 sums and verify all files have matching checksums:

`sha256sum --check {{filename.sha256}}`

- Only show a message for files for which verification fails:

`sha256sum --check --quiet {{filename.sha256}}`
