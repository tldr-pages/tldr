# uncompress

> Uncompress files compressed using the Unix `compress` command.
> More information: <https://linux.die.net/man/1/uncompress>.

- Uncompress specific files:

`uncompress {{path/to/file1.Z path/to/file2.Z ...}}`

- Uncompress specific files while ignoring non-existent ones:

`uncompress -force {{file1.Z file2.Z ...}}`

- Write to Standard Output (No Files Are Changed and No `.Z` Files Are Created):

`uncompress -c {{file1.Z file2.Z ...}}`

- Verbose Mode (Write to Standard Error About Percentage Reduction or Expansion):

`uncompress -v {{file1.Z file2.Z ...}}`

- Set the Upper Limit for Compression Ratio:

 `uncompress -b {{file1.Z file2.Z …}}`
