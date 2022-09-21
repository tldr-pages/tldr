# znew

> Recompress files from .Z to .gz format.
> More information: <https://www.gnu.org/software/gzip/manual/gzip.html>.

- Recompress a file from .Z to .gz format:

`znew {{file1.Z}}`

- Recompress multiple files and display the achieved size reduction per file:

`znew -v {{file1.Z}} {{file2.Z}} {{file3.Z}}`

- Recompress a file using the slowest (optimal) compression method:

`znew -9 {{file1.Z}}`

- Recompress a file, keeping the .Z file if it is smaller than the .gz file:

`znew -K {{file1.Z}}`
