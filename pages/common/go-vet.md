# go vet

> Check Go source code and report suspicious constructs (e.g. lint your Go source files).
> Go vet returns a non-zero exit code if problems are found; returns a zero exit code if no problems are found.
> More information: <https://pkg.go.dev/cmd/vet>.

- Check the Go package in the current directory:

`go vet`

- Check the Go package in the specified path:

`go vet {{path/to/file_or_directory}}`

- List available checks that can be run with go vet:

`go tool vet help`

- View details and flags for a particular check:

`go tool vet help {{check_name}}`

- Display offending lines plus N lines of surrounding context:

`go vet -c={{N}}`

- Output analysis and errors in JSON format:

`go vet -json`
