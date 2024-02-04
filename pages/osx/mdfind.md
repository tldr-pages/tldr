# mdfind

> List files matching a given query.
> More information: <https://keith.github.io/xcode-man-pages/mdfind.1.html>.

- Find a file by its name:

`mdfind -name {{file}}`

- Find a file by its content:

`mdfind "{{query}}"`

- Find a file containing a string, in a given directory:

`mdfind -onlyin {{directory}} "{{query}}"`
