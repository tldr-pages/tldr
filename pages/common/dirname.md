# dirname

> Remove trailing filename portion from a path.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/dirname-invocation.html>.

- Calculate the parent directory of a given path:

`dirname {{path/to/file_or_directory}}`

- Calculate the parent directory of multiple paths:

`dirname {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Delimit output with a NUL character instead of a newline (useful when combining with `xargs`):

`dirname {{[-z|--zero]}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`
