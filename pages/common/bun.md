# bun

> JavaScript runtime and toolkit.
> Includes a bundler, a test runner, and a package manager.
> More information: <https://bun.com/docs>.

- Create a new Bun project in the current directory:

`bun init`

- Run a JavaScript file or a `package.json` script:

`bun run {{path/to/file|script_name}}`

- Run unit tests:

`bun test`

- Download and install all the packages listed as dependencies in `package.json`:

`bun {{[i|install]}}`

- Add a dependency to `package.json`:

`bun {{[a|add]}} {{module_name}}`

- Remove a dependency from `package.json`:

`bun {{[rm|remove]}} {{module_name}}`

- Start a REPL (interactive shell):

`bun repl`

- Upgrade Bun to the latest version:

`bun upgrade`
