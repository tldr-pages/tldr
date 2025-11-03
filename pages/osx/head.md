# head

> Output the first part of files.
> More information: <https://keith.github.io/xcode-man-pages/head.1.html>.

- Output the first 10 lines of a file:

`head {{path/to/file}}`

- Output the first 5 lines of multiple files:

`head {{[-5|--lines 5]}} {{path/to/file1 path/to/file2 ...}}`

- Output the first `count` lines of a file:

`head {{[-n|--lines]}} {{count}} {{path/to/file}}`

- Output the first `n` bytes of a file:

`head {{[-c|--bytes]}} {{n}} {{path/to/file}}`
