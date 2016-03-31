# sha512sum

> Calculate SHA512 cryptographic checksums.

- Calculate the SHA384 checksum for a file:

`sha512sum {{filename1}}`

- Calculate SHA384 checksums for multiple files:

`sha512sum {{filename1}} {{filename2}}`

- Read a file of SHA512 sums and verify all files have matching checksums:

`sha512sum -c {{filename.sha512}}`
