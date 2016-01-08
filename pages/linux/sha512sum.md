# sha512sum

> Calculate SHA512 cryptographic checksums.

- Calculate the SHA512 checksum for file(s) or files in a directory, one checksum per file:

`sha512sum {{filename1}}`
`sha512sum {{filename1}} {{filename2}}`
`sha512sum {{directory/\*}}`

- Read a file of SHA512 sums and verify all files have matching checksums:

`sha512sum -c {{filename.sha512}}`
