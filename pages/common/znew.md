# znew

> Recompress files from `.Z` to gzip format.
> More information: <https://manned.org/znew>.

- Recompress a file from `.Z` to gzip format:

`znew {{path/to/file1.Z}}`

- Recompress multiple files and display the achieved size reduction % per file:

`znew -v {{path/to/file1.Z path/to/file2.Z ...}}`

- Recompress a file using the slowest compression method (for optimal compression):

`znew -9 {{path/to/file1.Z}}`

- Recompress a file, [K]eeping the `.Z` file if it is smaller than the gzip file:

`znew -K {{path/to/file1.Z}}`
