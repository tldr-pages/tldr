# go test

> Test Go packages (files have to end with `_test.go`).
> Note: `./...` is a Go package pattern understood by Go tooling. It matches the current package and all packages recursively under the current directory.
> More information: <https://pkg.go.dev/cmd/go#hdr-Testing_flags>.

- Test the package found in the current directory:

`go test`

- [v]erbosely test the package in the current directory:

`go test -v`

- Test the packages in the current directory and all subdirectories:

`go test -v ./...`

- Test the package in the current directory and run all benchmarks:

`go test -v -bench .`

- Test the package in the current directory and run all benchmarks for 50 seconds:

`go test -v -bench . -benchtime 50s`

- Test the package with coverage analysis:

`go test -cover`
