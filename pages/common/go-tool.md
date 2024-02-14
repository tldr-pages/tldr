# go tool

> Run a Go tool or command.
> Execute a Go command as a stand-alone binary, typically for debugging.
> More information: <https://pkg.go.dev/cmd/go#hdr-Run_specified_go_tool>.

- List available tools:

`go tool`

- Run the go link tool:

`go tool link {{path/to/main.o}}`

- Print the command that would be executed, but do not execute it (similar to `whereis`):

`go tool -n {{command}} {{arguments}}`

- View documentation for a specified tool:

`go tool {{command}} --help`
