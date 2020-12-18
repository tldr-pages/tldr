# sha512sum

> Calculate SHA512 cryptographic checksums.

- Calculate the SHA512 checksum for a file:

`sha512sum {{filename1}}`

- Calculate SHA512 checksums for multiple files:

`sha512sum {{filename1}} {{filename2}}`

- Read a file of SHA512 sums and verify all files have matching checksums:

`sha512sum --check {{filename.sha512}}`

- Verify all files have matching chesksums but don't print OK for succefully verified file:

`sha512sum --check --quiet {{filename.sha512}}`
