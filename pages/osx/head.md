# head

> Output the first part of files.
> More information: <https://keith.github.io/xcode-man-pages/head.1.html>.

- Output the first few lines of a file:

`head --lines {{count}} {{path/to/file}}`

- Output the first few bytes of a file:

`head --bytes {{count}} {{path/to/file}}`

- Output everything but the last few lines of a file:

`head --lines -{{count}} {{path/to/file}}`

- Output everything but the last few bytes of a file:

`head --bytes -{{count}} {{path/to/file}}`
