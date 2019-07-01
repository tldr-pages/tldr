# gofmt

> Tool for formatting Go source code.
> More information: <https://golang.org/cmd/gofmt/>.

- Format a file and display the result to the console:

`gofmt {{source.go}}`

- Format a file, overwriting the original file in-place:

`gofmt -w {{source.go}}`

- Format a file, and then simplify the code, overwriting the original file:

`gofmt -s -w {{source.go}}`

- Print all (including spurious) errors:

`gofmt -e {{source.go}}`
