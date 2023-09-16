# shar

> Create a shell archive.
> More information: <https://www.gnu.org/software/sharutils/manual/sharutils.html>.

- Create a shell script that when executed extracts the given files from itself:

`shar --vanilla-operation {{path/to/file1 path/to/file2 ...}} > {{path/to/archive.sh}}`

- Compress the files in the archive:

`shar --compactor {{xz}} {{path/to/file1 path/to/file2 ...}} > {{path/to/archive.sh}}`

- Treat all files as binary (i.e. `uuencode` everything):

`shar --uuencode {{path/to/file1 path/to/file2 ...}} > {{path/to/archive.sh}}`

- Treat all files as text (i.e. `uuencode` nothing):

`shar --text-files {{path/to/file1 path/to/file2 ...}} > {{path/to/archive.sh}}`

- Include a name and cut mark in the header comment of the archive:

`shar --archive-name "{{My files}}" --cut-mark {{path/to/file1 path/to/file2 ...}} > {{path/to/archive.sh}}`
