# md5

> Calculate MD5 cryptographic checksums.
> More information: <https://keith.github.io/xcode-man-pages/md5.1.html>.

- Calculate the MD5 checksum for a file:

`md5 {{path/to/file}}`

- Calculate MD5 checksums for multiple files:

`md5 {{path/to/file1 path/to/file2 ...}}`

- Output only the md5 checksum (no filename):

`md5 -q {{path/to/file}}`

- Print a checksum of the given string:

`md5 -s "{{string}}"`
