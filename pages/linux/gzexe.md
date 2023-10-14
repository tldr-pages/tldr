# gzexe

> Compress executable files while keeping them executable.
> Back up the original file, appending `~` to its name and create a shell script that uncompresses and executes the binary inside it.
> More information: <https://manned.org/gzexe.1>.

- Compress an executable file in-place:

`gzexe {{path/to/executable}}`

- Decompress a compressed executable in-place:

`gzexe -d {{path/to/compressed_executable}}`
