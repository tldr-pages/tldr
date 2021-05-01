# sha1sum

> Calculate SHA1 cryptographic checksums.
> More information: <https://www.gnu.org/software/coreutils/sha1sum>.

- Calculate the SHA1 checksum for a file:

`sha1sum {{filename1}}`

- Calculate SHA1 checksums for multiple files:

`sha1sum {{filename1}} {{filename2}}`

- Calculate and save the list of SHA1 checksums to a file:

`sha1sum {{filename1}} {{filename2}} > {{filename.sha1}}`

- Read a file of SHA1 sums and verify all files have matching checksums:

`sha1sum --check {{filename.sha1}}`

- Only show a message for files for which verification fails:

`sha1sum --check --quiet {{filename.sha1}}`
