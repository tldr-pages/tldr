# gzexe

> Compress executable files while keeping them executable.
> Back up the original file, appending `~` to its name and create a shell script that uncompresses and executes the binary inside it.
> More information: <https://manned.org/gzexe.1>.

- Compress an executable file in-place:

`gzexe {{path/to/executable}}`

- Decompress a compressed executable in-place (i.e. convert the shell script back to an uncompressed binary):

`gzexe -d {{path/to/compressed_executable}}`
