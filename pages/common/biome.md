# biome

> A toolchain for formatting, linting, and checking code quality for web projects.
> More information: <https://biomejs.dev/reference/cli/>.

- Initialize a new Biome configuration file in the current directory:

`biome init`

- Format files and overwrite them in place:

`biome format --write {{path/to/file_or_directory}}`

- Check formatting without applying changes:

`biome format {{path/to/file_or_directory}}`

- Lint files and apply safe fixes:

`biome lint --write {{path/to/file_or_directory}}`

- Run format, lint, and import sorting, applying safe fixes:

`biome check --write {{path/to/file_or_directory}}`

- Run all checks in CI mode (no fixes applied, exits with error if issues found):

`biome ci {{path/to/file_or_directory}}`

- Explain a specific lint rule:

`biome explain {{rule_name}}`

- Display version:

`biome {{[-V|--version]}}`
