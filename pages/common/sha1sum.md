# sha1sum

> Calculate SHA1 cryptographic checksums.

- Calculate the SHA1 checksum for a file:

`sha1sum {{filename1}}`

- Calculate SHA1 checksums for multiple files:

`sha1sum {{filename1}} {{filename2}}`

- Read a file of SHA1 sums and verify all files have matching checksums:

`sha1sum -c {{filename.sha1}}`

- Verify all files have matching chesksums but don't print OK for succefully verified file:

`sha1sum -c --quiet {{filename.sha1}}`
