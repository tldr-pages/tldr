# go get

> In Module mode, add dependency package.
> More information: <https://pkg.go.dev/cmd/go#hdr-Add_dependencies_to_current_module_and_install_them>.

- In module-mode, add package to go.mod:

`go get example.com/pkg`

- In module-mode, modify the packge with version:

`go get example.com/pkg@v1.2.3`

- In module-mode, remove the packge:

`go get example.com/pkg@none`

> In GOPATH mode, download packages into $GOPTAH/src.
> More information: <https://pkg.go.dev/cmd/go#hdr-Legacy_GOPATH_go_get>.

- In GOPATH-mode, download and install the packge:

`go get example.com/pkg`
