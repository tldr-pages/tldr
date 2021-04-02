# sha384sum

> Calculate SHA384 cryptographic checksums.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Calculate the SHA384 checksum for a file:

`sha384sum {{filename1}}`

- Calculate SHA384 checksums for multiple files:

`sha384sum {{filename1}} {{filename2}}`

- Calculate and save the list of SHA384 checksums to a file:

`sha384sum {{filename1}} {{filename2}} > {{filename.sha384}}`

- Read a file of SHA384 sums and verify all files have matching checksums:

`sha384sum --check {{filename.sha384}}`

- Only show a message for files for which verification fails:

`sha384sum --check --quiet {{filename.sha384}}`
