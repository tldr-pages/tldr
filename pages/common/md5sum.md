# md5sum

> Calculate MD5 cryptographic checksums.
> More information: <https://www.gnu.org/software/coreutils/md5sum>.

- Calculate the MD5 checksum for a file:

`md5sum {{filename1}}`

- Calculate MD5 checksums for multiple files:

`md5sum {{filename1}} {{filename2}}`

- Read a file of MD5SUMs and verify all files have matching checksums:

`md5sum -c {{filename.md5}}`

- Calculate a MD5 checksum from the standard input:

`echo "{{text}}" | md5sum`
