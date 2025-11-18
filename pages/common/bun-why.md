# bun why

> Explain why a package is installed by showing its dependency chain.
> More information: <https://bun.com/docs/pm/cli/why>.

- Explain why a specific package is installed:

`bun why {{package_name}}`

- Explain why all packages matching a pattern are installed:

`bun why "{{pattern}}"`

- Explain why packages from a specific organization are installed:

`bun why "{{@organization/*}}"`

- Show only top-level dependencies:

`bun why {{package_name}} --top`

- Limit the dependency tree depth:

`bun why {{package_name}} --depth {{number}}`
