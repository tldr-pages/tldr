# go

> Tool for managing go source code.
> Some subcommands such as `go build` have their own usage documentation.
> More information: <https://golang.org>.

- Download and install a package, specified by its import path:

`go get {{package_path}}`

- Compile and run a source file (it has to contain a `main` package):

`go run {{path/to/file}}.go`

- Compile a source file into a named executable:

`go build -o {{path/to/executable}} {{path/to/file}}.go`

- Compile the package present in the current directory:

`go build`

- Execute all test cases of the current package (files have to end with `_test.go`):

`go test`

- Compile and install the current package:

`go install`

- Initialize a new module in the current directory:

`go mod init {{module_name}}`
