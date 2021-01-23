# sha224sum

> Calculate SHA224 cryptographic checksums.

- Calculate the SHA224 checksum for a file:

`sha224sum {{filename1}}`

- Calculate SHA224 checksums for multiple files:

`sha224sum {{filename1}} {{filename2}}`

- Calculate and save the list of SHA224 checksums to a file:

`sha224sum {{filename1}} {{filename2}} > {{filename.sha224}}`

- Read a file of SHA224 sums and verify all files have matching checksums:

`sha224sum --check {{filename.sha224}}`

- Only show a message for files for which verification fails:

`sha224sum --check --quiet {{filename.sha224}}`
