# go doc

> Show documentation for package or symbol.
> More information: <https://golang.org/cmd/go/#hdr-Show_documentation_for_package_or_symbol>.

- Show documentation for current package:

`go doc`

- Show package documentation and exported symbols:

`go doc {{encoding/json}}`

- Show also documentation of symbols:

`go doc -all {{encoding/json}}`

- Show also sources:

`go doc -all -src {{encoding/json}}`

- Show a specific symbol:

`go doc -all -src {{encoding/json.Number}}`
