# sha384sum

> Calculate SHA384 cryptographic checksums.

- Calculate the SHA384 checksum for file(s) or files in a directory, one checksum per file:

`sha384sum {{filename1}}`
`sha384sum {{filename1}} {{filename2}}`
`sha384sum {{directory/\*}}`

- Read a file of SHA384 sums and verify all files have matching checksums:

`sha384sum -c {{filename.sha384}}`
