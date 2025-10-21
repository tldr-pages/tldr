# head

> Output the first part of files.
> More information: <https://keith.github.io/xcode-man-pages/head.1.html>.

- Output the first 10 lines of a file:

`head {{path/to/file}}`

- Output the first N lines of a file:

`head {{[-n|--lines]}} {{count}} {{path/to/file}}`

- Output the first N bytes of a file:

`head {{[-c|--bytes]}} {{bytes}} {{path/to/file}}`

- Output the first lines of multiple files:

`head {{path/to/file1 path/to/file2 ...}}`
