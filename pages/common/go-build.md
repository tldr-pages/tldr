# go build

> Compile Go sources.
> More information: <https://golang.org/cmd/go/#hdr-Compile_packages_and_dependencies>.

- Compile a file:

`go build path/to/main.go`

- Compile into named output:

`go build -o {{binary}} path/to/source.go`

- Compile a package:

`go build -o {{binary}} path/to/package`

- Compile a main package into an executable, with data race detection:

`go build -race -o {{executable}} path/to/main/package`
