# go tool

> Run a specified Go tool command.
> More information: <https://pkg.go.dev/cmd/go#hdr-Run_specified_go_tool>.

- Print the list of known Go tool commands:

`go tool`

- Show documentation about a particular Go tool command:

`go doc cmd/{{command}}`

- Run a Go tool command:

`go tool {{command}}`

- Print the command that would be executed for a Go tool command, but do not execute it:

`go tool -n {{command}}`
