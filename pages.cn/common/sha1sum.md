# sha1sum

> Calculate SHA1 cryptographic checksums.

- Calculate the SHA1 checksum for a file:

`sha1sum {{filename1}}`

- Calculate SHA1 checksums for multiple files:

`sha1sum {{filename1}} {{filename2}}`

- Read a file of SHA1 sums and verify all files have matching checksums:

`sha1sum -c {{filename.sha1}}`
