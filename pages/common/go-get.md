# go get

> Add a dependency package, or download packages in legacy GOPATH mode.
> Note: `./...` is a Go package pattern understood by Go tooling. It matches the current package and all packages recursively under the current directory.
> More information: <https://pkg.go.dev/cmd/go#hdr-Add_dependencies_to_current_module_and_install_them>.

- Add a specified package to `go.mod` in module-mode or install the package in GOPATH-mode:

`go get {{example.com/pkg}}`

- Modify the package with a given version in module-aware mode:

`go get {{example.com/pkg}}@{{v1.2.3}}`

- Remove a specified package:

`go get {{example.com/pkg}}@{{none}}`

- Update a package to its latest release:

`go get -u example.com/pkg`

- Update direct dependencies:

`go get -u`

- Update direct and indirect dependencies:

`go get -u ./...`

- Update direct, indirect, and test dependencies:

`go get -u -t ./...`
