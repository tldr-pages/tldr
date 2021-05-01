# pnpx

> Execute binaries from `npm` packages.
> Uses PNPM instead of NPM to execute packages.
> More information: <https://pnpm.io/pnpx-cli>.

- Execute the binary from a given npm module:

`pnpx {{module_name}}`

- In case a package has multiple binaries, specify the package name along with the binary:

`pnpx -p {{package_name}} {{module_name}}`

- Show help:

`pnpx --help`
