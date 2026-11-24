# lua-language-server

> Language Server Protocol implementation for Lua.
> More information: <https://luals.github.io/wiki/usage/>.

- Perform a diagnosis report, including code style checks if enabled:

`lua-language-server --check {{path/to/project}}`

- Perform a diagnosis report with the specified check level (defaults to Warning):

`lua-language-server --check {{path/to/project}} --checklevel {{Error|Warning|Information|Hint}}`
