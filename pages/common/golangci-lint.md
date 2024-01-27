# golangci-lint

> Smart, fast linters runner for Go.
> More information: <https://golangci-lint.run/>.

- Run linters in current folder

`golangci-lint run`

- List enabled/disabled linters (note: disabled linters are shown last, do not mistake them for enabled ones)

`golangci-lint linters`

- Enable a specific linter for this run

`golangci-lint run -E linterToEnable`
