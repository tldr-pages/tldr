# shar

> Create a shell archive.
> More information: <https://manned.org/shar.1>.

- Specify compression for input files:

`shar -p --intermix-type`

- Specify compaction (compression) program:

`shar -C {{program}} --compactor={{program}}`

- Pass level for compression:

`shar -g {{level}} --level-of-compression={{level}}`

- Decide uuencoding for each file:

`shar -M, --mixed-uuencode`

- Treat all files as binary:

`shar -B, --uuencode`

- Treat all files as text:

`shar -T, --text-files`
