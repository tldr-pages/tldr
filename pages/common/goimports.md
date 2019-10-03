# goimports

> Updates your Go import lines, adding missing ones and removing unreferenced ones.
> More information: <https://godoc.org/golang.org/x/tools/cmd/goimports>.

- Display diffs instead of rewriting file:

`goimports -d {{file}}.go`

- Write the result to the source file instead of the standard output:

`goimports -w {{file}}.go`

- Display diffs and write the result to the source file:

`goimports -w -d {{file}}.go`
