# npx

> Execute binaries from `npm` packages.
> More information: <https://github.com/npm/npx>.

- Execute the binary from a given npm module:

`npx {{module_name}} {{command_arguments}}`

- In case a package has multiple binaries, specify the package name along with the binary:

`npx --package {{package_name}} {{module_name}}`

- Run a command if it exists in the current path or in `node_modules/.bin`:

`npx --no-install {{command}} {{command_arguments}}`

- Execute the binary from a given npm module suppressing any output from `npx` itself:

`npx --quiet {{module_name}} {{command_arguments}}`

- Display help:

`npx --help`
