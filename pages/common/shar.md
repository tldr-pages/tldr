# shar

> Create a shell archive.
> More information: <https://manned.org/shar>.

- Specify compression for input files:

`shar --intermix-type`

- Specify compaction (compression) program:

`shar --compactor={{program}}`

- Pass level for compression:

`shar -g {{level}} --level-of-compression={{level}}`

- Decide uuencoding for each file:

`shar --mixed-uuencode`

- Treat all files as binary:

`shar -B, --uuencode`

- Treat all files as text:

`shar --text-files`
