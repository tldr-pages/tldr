# dirname

> Calculates the parent directory of a given file or directory path.
> More information: <https://www.gnu.org/software/coreutils/dirname>.

- Calculate the parent directory of a given path:

`dirname {{path/to/file_or_directory}}`

- Calculate the parent directory of multiple paths:

`dirname {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Delimit output with a NUL character instead of a newline (useful when combining with `xargs`):

`dirname --zero {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`
