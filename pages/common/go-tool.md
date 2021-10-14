# go tool

> Run a specific Go tool or command.
> Execute a Go command as a stand-alone binary, typically for debugging.
> More information: <https://pkg.go.dev/cmd/go#hdr-Run_specified_go_tool>.

- List available tools:

`go tool`

- Run the go link tool:

`go tool link main.o`

- Print the command that would be executed, but do not execute it:

`go tool -n dist clean`

- Display documentation for a specified tool:

`go doc cmd/{{tool}`
