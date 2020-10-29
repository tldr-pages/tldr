# goimports

> Updates Go import lines, adding missing ones and removing unreferenced ones.
> More information: <https://godoc.org/golang.org/x/tools/cmd/goimports>.

- Display the completed import source file:

`goimports {{file}}.go`

- Write the result back to the source file instead of the standard output:

`goimports -w {{file}}.go`

- Display diffs and write the result back to the source file:

`goimports -w -d {{file}}.go`

- Set the import prefix string after 3rd-party packages (comma-separated list):

`goimports -local {{path/to/package}} {{file}}.go`
