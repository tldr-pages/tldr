# npm exec

> Execute binaries from `npm` packages.
> More information: <https://docs.npmjs.com/cli/npm-exec>.

- Execute the command from a local or remote `npm` package:

`npm {{[x|exec]}} {{command}} {{argument1 argument2 ...}}`

- In case multiple commands with the same name exist, it is possible to explicitly specify the package:

`npm {{[x|exec]}} --package {{package}} {{command}}`

- Run a command if it exists in the current path or in `node_modules/.bin`:

`npm {{[x|exec]}} --no-install {{command}} {{argument1 argument2 ...}}`

- Execute a specific command suppressing any output from `npm` itself:

`npm {{[x|exec]}} --quiet {{command}} {{argument1 argument2 ...}}`

- Display help:

`npm {{[x|exec]}} --help`
