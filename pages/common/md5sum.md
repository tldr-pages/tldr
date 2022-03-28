# md5sum

> Calculate MD5 cryptographic checksums.
> More information: <https://www.gnu.org/software/coreutils/md5sum>.

- Calculate the MD5 checksum for a file:

`md5sum {{path/to/file}}`

- Calculate MD5 checksums for multiple files:

`md5sum {{path/to/file1}} {{path/to/filen2}}`

- Calculate a MD5 checksum from the standard input:

`echo "{{text}}" | md5sum`

- Read a file of MD5SUMs and verify all files have matching checksums:

`md5sum --check {{path/to/file.md5}}`

- Only show a message for missing files or when verification fails:

`md5sum --check --quiet {{path/to/file.md5}}`

- Only show a message for files for which verification fails, ignoring missing files:

`md5sum --ignore-missing --check --quiet {{path/to/file.md5}}`
