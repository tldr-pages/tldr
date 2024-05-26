# golangci-lint

> Parallelized, smart and fast Go linters runner that integrates with all major IDEs and supports YAML configuration.
> More information: <https://golangci-lint.run/welcome/quick-start/>.

- Run linters in the current folder:

`golangci-lint run`

- List enabled and disabled linters (Note: disabled linters are shown last, do not mistake them for enabled ones):

`golangci-lint linters`

- [E]nable a specific linter for this run:

`golangci-lint run --enable {{linter}}`
