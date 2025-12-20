# trunk

> Run linters, formatters, and security analyzers on code.
> More information: <https://docs.trunk.io/code-quality/overview/getting-started/commands-reference>.

- Initialize trunk in a repository:

`trunk init`

- Run all applicable linters and formatters on changed files:

`trunk check`

- Run linters and formatters on specific files:

`trunk check {{path/to/file1 path/to/file2 ...}}`

- Format files in place:

`trunk fmt`

- List all available tools and their status:

`trunk tools list`

- Enable a tool at a specific version:

`trunk tools enable {{tool}}@{{version}}`

- Print an action's execution history:

`trunk actions history {{action}}`
