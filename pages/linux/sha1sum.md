# sha1sum

> Calculate SHA1 cryptographic checksums.

- Calculate the SHA1 checksum for file(s) or files in a directory, one checksum per file:

`sha1sum {{filename1}}`
`sha1sum {{filename1}} {{filename2}}`
`sha1sum {{directory/\*}}`

- Read a file of SHA1 sums and verify all files have matching checksums:

`sha1sum -c {{filename.sha1}}`
