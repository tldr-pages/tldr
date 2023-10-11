# npx

> Execute binaries from `npm` packages.
> More information: <https://github.com/npm/npx>.

- Execute the command from a local or remote `npm` package:

`npx {{command}} {{argument1 argument2 ...}}`

- In case multiple commands with the same name exist, it is possible to explicitly specify the package:

`npx --package {{package}} {{command}}`

- Run a command if it exists in the current path or in `node_modules/.bin`:

`npx --no-install {{command}} {{argument1 argument2 ...}}`

- Execute a specific command suppressing any output from `npx` itself:

`npx --quiet {{command}} {{argument1 argument2 ...}}`

- Display help:

`npx --help`
