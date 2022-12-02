# gofmt

> Tool for formatting Go source code.
> More information: <https://golang.org/cmd/gofmt/>.

- Format a file and display the result to the console:

`gofmt {{path/to/source.go}}`

- Format a file, overwriting the original file in-place:

`gofmt -w {{path/to/source.go}}`

- Format a file, and then simplify the code, overwriting the original file:

`gofmt -s -w {{path/to/source.go}}`

- Print all (including spurious) errors:

`gofmt -e {{path/to/source.go}}`
