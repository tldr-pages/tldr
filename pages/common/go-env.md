# go env

> Manage environment variables used by the Go toolchain.
> More information: <https://golang.org/cmd/go/#hdr-Print_Go_environment_information>.

- Show all environment variables:

`go env`

- Show an environment variable:

`go env {{GOPATH}}`

- Set an environment value:

`go env -w {{GOBIN}}={{path/to/directory}}`

- Reset an environment value:

`go env -u {{GOBIN}}`
