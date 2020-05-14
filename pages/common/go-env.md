# go env

> Manage environment variables used by the Go toolchain.
> More information: <https://golang.org/cmd/go/#hdr-Print_Go_environment_information>.

- Show all environment variables:

`go env`

- Show a specific environment variable:

`go env {{GOPATH}}`

- Set an environment variable to a value:

`go env -w {{GOBIN}}={{path/to/directory}}`

- Reset an environment variable's value:

`go env -u {{GOBIN}}`
