# go clean

> Tool for removing object files and cached files.
> More information: <https://golang.org/cmd/go/>.

- Print the remove commands only:

`go clean -n`

- Remove go build cache:

`go clean -cache`

- Remove all test results in the go build cache :

`go clean -testcache`

- Remove go module download cache:

`go clean -modcache`

- Remove all:

`go clean -cache -testcache -modcache -i -r`
