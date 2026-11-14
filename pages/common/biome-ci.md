# biome-ci

> Run Biome formatting, linting, and import sorting checks in continuous integration environments.
> More information: <https://biomejs.dev/reference/cli/#biome-ci>.

- Check formatting, linter rules, and import organization across the current project without modifying files:

`biome ci .`

- Run CI checks only on files changed since a specific Git branch:

`biome ci --changed --since={{origin/main}}`

- Specify the maximum number of diagnostics to print before truncating output:

`biome ci --max-diagnostics={{50}} {{path/to/directory}}`
