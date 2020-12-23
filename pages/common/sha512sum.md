# sha512sum

> Calculate SHA512 cryptographic checksums.

- Calculate the SHA512 checksum for a file:

`sha512sum {{filename1}}`

- Calculate SHA512 checksums for multiple files:

`sha512sum {{filename1}} {{filename2}}`

- Calculate and save the list of SHA512 checksums to a file:

`sha512sum {{filename1}} {{filename2}} > {{filename.sha512}}`

- Read a file of SHA512 sums and verify all files have matching checksums:

`sha512sum --check {{filename.sha512}}`

- Only show a message for files for which verification fails:

`sha512sum --check --quiet {{filename.sha512}}`
