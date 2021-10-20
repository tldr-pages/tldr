# go install

> Compile and install packages named by the import paths.
> More information: <https://pkg.go.dev/cmd/go#hdr-Compile_and_install_packages_and_dependencies>.

- Compile and install current package:

`go install`

- Compile and install a local package:

`go install {{./cmd/...}}`

- Install the latest version of a program, ignoring `go.mod` in the current directory (if any):

`go install {{golang.org/x/tools/gopls}}@{{latest}}`

- Install a program at the version selected by the module in the current directory:

`go install {{golang.org/x/tools/gopls}}`
