# dirname

> Calculates the parent directory of a given file or directory path.

- Calculate the parent directory of a given file path:

`dirname {{path/to/file_or_directory}}`

- Calculate the parent directory of multiple paths:

`dirname {{path/to/file_a}} {{path/to/file_b}}`

- Delimit output with a NUL character instead of a newline (useful when combining with `xargs`):

`dirname --zero {{path/to/file_a}} {{path/to/file_b}}`
