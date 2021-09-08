# go get

> In Module mode, add dependency package.
> More information: <https://pkg.go.dev/cmd/go#hdr-Add_dependencies_to_current_module_and_install_them>.
> In GOPATH mode, download packages into $GOPTAH/src.
> More information: <https://pkg.go.dev/cmd/go#hdr-Legacy_GOPATH_go_get>.

- Add the package to go.mod in module-mode or install the packge in GOPATH-mode:

`go get {{example.com/pkg}}`

- In module-mode, modify the package with a given version:

`go get {{example.com/pkg@v1.2.3}}`

- In module-mode, remove the package:

`go get {{example.com/pkg@none}}`
