# gofmt

> Tool for formatting Go source code.

- Format a file and display the result to the console:

`gofmt {{source.go}}`

- Format a file, overwriting the original file in-place:

`gofmt {{source.go}} -w`

- Format a file, and then simplify the code, overwriting the original file:

`gofmt {{source.go}} -s -w`

- Print all (including spurious) errors:

`gofmt {{source.go}} -e`
