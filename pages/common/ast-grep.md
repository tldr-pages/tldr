# ast-grep

> Search, lint, and rewrite code using AST patterns.
> More information: <https://ast-grep.github.io/reference/cli.html>.

- Search for a pattern in files:

`ast-grep run {{[-p|--pattern]}} '{{pattern}}' {{path/to/file}}`

- Search for a pattern in a specific language:

`ast-grep run {{[-p|--pattern]}} '{{pattern}}' {{[-l|--lang]}} {{python}} {{path/to/directory}}`

- Rewrite code matching a pattern:

`ast-grep run {{[-p|--pattern]}} '{{pattern}}' {{[-r|--rewrite]}} '{{replacement}}' {{path/to/file}}`

- Display help for a subcommand:

`ast-grep {{run}} {{[-h|--help]}}`

- Run rules from a configuration file:

`ast-grep scan {{[-r|--rule]}} {{path/to/rule.yml}} {{path/to/directory}}`

- Interactively search and rewrite code:

`ast-grep run {{[-p|--pattern]}} '{{pattern}}' {{[-i|--interactive]}} {{path/to/directory}}`
