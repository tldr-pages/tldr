# uncompress

> Uncompress files compressed using the Unix `compress` command.
> More information: <https://linux.die.net/man/1/uncompress>.

- Uncompress specific files:

`uncompress {{path/to/file1.Z path/to/file2.Z ...}}`

- Uncompress specific files while ignoring non-existent ones:

`uncompress -force {{path/to/file1.Z path/to/file2.Z ...}}`

- Write to standard output (no files are changed and no `.Z` files are created):

`uncompress -c {{path/to/file1.Z path/to/file2.Z ...}}`

- Verbose mode (write to standard error about percentage reduction or expansion):

`uncompress -v {{path/to/file1.Z path/to/file2.Z ...}}`

- Set the upper limit for compression ratio:

`uncompress -b {{path/to/file1.Z path/to/file2.Z ...}}`
