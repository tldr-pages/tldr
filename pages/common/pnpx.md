# pnpx

> Execute binaries from `npm` packages.
> Uses PNPM instead of NPM to execute packages.
> More information: <https://pnpm.io/pnpx-cli>.

- Execute the binary from a given npm module:

`pnpx {{module_name}}`

- Execute a specific binary from a given npm module, in case the module has multiple binaries:

`pnpx -p {{package_name}} {{module_name}}`

- Show help:

`pnpx --help`
