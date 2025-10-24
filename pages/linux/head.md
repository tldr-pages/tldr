# head

> Output the first part of files.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/head-invocation.html>.

- Show first 10 lines in a file:

`head {{path/to/file}}`

- Show first 10 lines of multiple files:

`head {{path/to/file1 path/to/file2 ...}}`

- Output the first 5 lines of a file:

`head {{[-5|--lines 5]}} {{path/to/file}}`

- Output the first few lines of a file:

`head {{[-n|--lines]}} {{count}} {{path/to/file}}`

- Output the first few bytes of a file:

`head {{[-c|--bytes]}} {{count}} {{path/to/file}}`

- Output everything but the last few lines of a file:

`head {{[-n|--lines]}} -{{count}} {{path/to/file}}`

- Output everything but the last few bytes of a file:

`head {{[-c|--bytes]}} -{{count}} {{path/to/file}}`
