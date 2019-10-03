# goimports

> Updates your Go import lines, adding missing ones and removing unreferenced ones.
> More information: <https://godoc.org/golang.org/x/tools/cmd/goimports>.

- Display diffs instead of rewriting file:

`goimports -d {{file}}.go`

- Write result to (source) file instead of stdout:

`goimports -w {{file}}.go`

- Display diffs and write result to (source) file:

`goimports -w -d {{file}}.go`
