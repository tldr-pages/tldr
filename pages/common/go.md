# go

> Tool for managing go source code.

- Download and install a package, specified by its import path:

`go get {{package_path}}`

- Compile and run a source file (it has to contain a `main` package):

`go run {{file}}.go`

- Compile the package present in the current directory:

`go build`

- Compile the file source.go into a named executable:

`go build -o executable source.go`

- Execute all test cases of the current package (files have to end with `_test.go`):

`go test`

- Compile and install the current package:

`go install`
