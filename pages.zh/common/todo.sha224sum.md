# sha224sum

> Calculate SHA224 cryptographic checksums.

- Calculate the SHA224 checksum for a file:

`sha224sum {{filename1}}`

- Calculate SHA224 checksums for multiple files:

`sha224sum {{filename1}} {{filename2}}`

- Read a file of SHA224 sums and verify all files have matching checksums:

`sha224sum -c {{filename.sha224}}`
