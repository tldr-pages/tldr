# biome

> A fast formatter and linter for JavaScript, TypeScript, JSX, JSON, CSS, and GraphQL.
> See also: `prettier`, `eslint`.
> More information: <https://biomejs.dev/reference/cli/>.

- Create a configuration file with some defaults:

`biome init`

- Lint, format, and sort imports for files or directories, applying safe fixes:

`biome check --write {{path/to/file_or_directory}}`

- Lint files or directories without formatting or sorting imports, applying safe fixes:

`biome lint --write {{path/to/file_or_directory}}`

- Format files or directories, replacing the original:

`biome format --write {{path/to/file_or_directory}}`

- Check formatting, linting, and import sorting without writing changes (intended for CI):

`biome ci {{path/to/file_or_directory}}`

- Migrate the configuration file from a previous Biome version:

`biome migrate --write`
