# mdfind

> List files matching a given query.
> More information: <https://ss64.com/osx/mdfind.html>.

- Find a file by its name:

`mdfind -name {{file}}`

- Find a file by its content:

`mdfind "{{query}}"`

- Find a file containing a string, in a given directory:

`mdfind -onlyin {{directory}} "{{query}}"`
