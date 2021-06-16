# go test

> Tests Go packages (files have to end with `_test.go`).
> More information: https://golang.org/cmd/go/#hdr-Testing_flags

- Test the package found at the current directory.
`go test`

- [v]erbosely test the package at the current directory.
`go test -v`

- [v]erbosely test the packages at the current directory and all subdirectories.
`go test -v ./...`

- [v]erbosely test the package at the current directory and run all benchmarks.
`go test -v -bench .`

- [v]erbosely test the package at the current directory and run all benchmarks for 50 seconds.
`go test -v -bench . -benchtime 50s`
