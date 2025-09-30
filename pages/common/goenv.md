# goenv

> Install, uninstall or switch between Golang versions.
> Supports version numbers like "1.16.15" or "1.22.8" etc.
> More information: <https://github.com/go-nv/goenv>.

- List all available goenv commands:

`goenv commands`

- Install a specific version of Golang:

`goenv install {{go_version}}`

- Use a specific version of Golang in the current project:

`goenv local {{go_version}}`

- Set the default Golang version:

`goenv global {{go_version}}`

- List all available Golang versions and highlight the default one:

`goenv versions`

- Uninstall a given Go version:

`goenv uninstall {{go_version}}`

- Run an executable with the selected Go version:

`goenv exec go run {{go_version}}`
