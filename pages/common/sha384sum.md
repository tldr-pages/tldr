# sha384sum

> Calculate SHA384 cryptographic checksums.

- Calculate the SHA384 checksum for a file:

`sha384sum {{filename1}}`

- Calculate SHA384 checksums for multiple files:

`sha384sum {{filename1}} {{filename2}}`

- Read a file of SHA384 sums and verify all files have matching checksums:

`sha384sum -c {{filename.sha384}}`

- Verify all files have matching chesksums but don't print OK for succefully verified file:

`sha384sum -c --quiet {{filename.sha384}}`
