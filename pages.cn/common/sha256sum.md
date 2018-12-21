# sha256sum

> Calculate SHA256 cryptographic checksums.

- Calculate the SHA256 checksum for a file:

`sha256sum {{filename1}}`

- Calculate SHA256 checksums for multiple files:

`sha256sum {{filename1}} {{filename2}}`

- Read a file of SHA256 sums and verify all files have matching checksums:

`sha256sum -c {{filename.sha256}}`
