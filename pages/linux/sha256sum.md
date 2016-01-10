# sha256sum

> Calculate SHA256 cryptographic checksums.

- Calculate the SHA256 checksum for file(s) or files in a directory, one checksum per file:

`sha256sum {{filename1}}`
`sha256sum {{filename1}} {{filename2}}`
`sha256sum {{directory/\*}}`

- Read a file of SHA256 sums and verify all files have matching checksums:

`sha256sum -c {{filename.sha256}}`
