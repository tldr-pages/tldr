# bun exec

> Execute a shell script directly with Bun.
> Note: When running from a shell, remember to escape quotes.
> More information: <https://bun.sh/docs/runtime/shell>.

- Run a simple command:

`bun exec "echo hello"`

- Run a command with flags:

`bun exec "ls -la"`

- Run a command containing quotes:

`bun exec "echo \"hello friends\""`

- Run a combined shell command:

`bun exec "mkdir test && cd test"`
