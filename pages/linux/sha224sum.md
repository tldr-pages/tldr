# sha224sum

> Calculate SHA224 cryptographic checksums.

- Calculate the SHA224 checksum for file(s) or files in a directory, one checksum per file:

`sha224sum {{filename1}}`
`sha224sum {{filename1}} {{filename2}}`
`sha224sum {{directory/\*}}`

- Read a file of SHA224 sums and verify all files have matching checksums:

`sha224sum -c {{filename.sha224}}`
