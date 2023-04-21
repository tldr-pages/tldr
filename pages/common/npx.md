# npx

> Execute binaries from `npm` packages.
> More information: <https://github.com/npm/npx>.

- Execute the command from a local or remote `npm` package:

`npx {{command}} {{arg1 arg2 ...}}`

- In case multiple commands with the same name exist, it is possible to specify the package name:

`npx --package {{package_name}} {{command}}`

- Run a command if it exists in the current path or in `node_modules/.bin`:

`npx --no-install {{command}} {{command_arguments}}`

- Execute a specific command suppressing any output from `npx` itself:

`npx --quiet {{command}} {{arg1 arg2 ...}}`

- Display help:

`npx --help`
