# go list

> List packages or modules.
> Note: `./...` is a Go package pattern understood by Go tooling. It matches the current package and all packages recursively under the current directory.
> More information: <https://pkg.go.dev/cmd/go#hdr-List_packages_or_modules>.

- List packages:

`go list ./...`

- List standard packages:

`go list std`

- List packages in JSON format:

`go list -json time net/http`

- List module dependencies and available updates:

`go list -m -u all`
