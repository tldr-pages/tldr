# biome ci

> Run Biome format, lint, and import sorting checks in continuous integration environments.
> More information: <https://biomejs.dev/reference/cli/#biome-ci>.

- Run format, lint, and assist checks on all files in the current project:

`biome ci`

- Run checks on specific files or directories:

`biome ci {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Run checks only on files changed since a specific Git branch:

`biome ci --changed --since={{main}}`

- Specify a custom maximum number of diagnostics to print:

`biome ci --max-diagnostics={{50}}`
