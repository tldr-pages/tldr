# go get

> Add a dependency package, or download packages in legacy GOPATH mode.
> More information: <https://pkg.go.dev/cmd/go#hdr-Add_dependencies_to_current_module_and_install_them>.

- Add a specified package to go.mod in module-mode or install the package in GOPATH-mode:

`go get {{example.com/pkg}}`

- In module-mode, modify the package with a given version:

`go get {{example.com/pkg@v1.2.3}}`

- In module-mode, remove the package:

`go get {{example.com/pkg@none}}`
