# head

> Output the first part of files.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/head-invocation.html>.

- Output the first few lines of a file:

`head {{[-n|--lines]}} {{count}} {{path/to/file}}`

- Output the first few bytes of a file:

`head {{[-c|--bytes]}} {{count}} {{path/to/file}}`

- Output everything but the last few lines of a file:

`head {{[-n|--lines]}} -{{count}} {{path/to/file}}`

- Output everything but the last few bytes of a file:

`head {{[-c|--bytes]}} -{{count}} {{path/to/file}}`
