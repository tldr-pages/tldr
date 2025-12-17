# gofumpt

> Strictly format Go files.
> See also: `gofmt`.
> More information: <https://pkg.go.dev/mvdan.cc/gofumpt>.

- Format go files:

`gofumpt -w {{path/to/directory}}`

- List files whose formatting differs from `gofumpt`:

`gofumpt -l {{path/to/directory}}`

- Report all errors:

`gofumpt -e {{path/to/directory}}`

- Display diffs:

`gofumpt -d {{path/to/directory}}`

- Display help:

`gofumpt {{[-h|--help]}}`
