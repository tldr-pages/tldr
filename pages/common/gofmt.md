# gofmt

> Format Go source code.
> More information: <https://pkg.go.dev/cmd/gofmt>.

- Format a file and display the result to the console:

`gofmt {{path/to/source.go}}`

- Format a file, overwriting the original file in-place:

`gofmt -w {{path/to/source.go}}`

- Format a file, and then simplify the code, overwriting the original file:

`gofmt -s -w {{path/to/source.go}}`

- Display diffs instead of rewriting files:

`gofmt -d {{path/to/source.go}}`

- List files that would be changed by gofmt:

`gofmt -l {{path/to/directory}}`

- Apply a rewrite rule to the source before reformatting (e.g. replace nil checks with `isNil` calls):

`gofmt -r '{{x == nil -> isNil(x)}}' {{path/to/source.go}}`

- Report all errors, including multiple ones per line:

`gofmt -e {{path/to/source.go}}`
