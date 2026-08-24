# govulncheck

> Report known vulnerabilities that affect Go code.
> Note: `./...` is a Go package pattern understood by Go tooling. It matches the current package and all packages recursively under the current directory.
> More information: <https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck>.

- Scan the current module and its dependencies for vulnerabilities:

`govulncheck ./...`

- Scan a specific package:

`govulncheck {{path/to/package}}`

- Scan a Go binary instead of source code:

`govulncheck -mode binary {{path/to/binary}}`

- Extract build information and build information from a go binary:

`govulncheck -mode extract {{path/to/binary}}`

- Scan test files as well:

`govulncheck -test ./...`

- Print the results in a specific format:

`govulncheck -format {{text|json|sarif|openvex}} ./...`

- Display the call stacks leading to each vulnerable symbol:

`govulncheck -show traces ./...`
