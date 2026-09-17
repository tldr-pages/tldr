# typos

> Find and correct spelling mistakes in source code.
> More information: <https://github.com/crate-ci/typos/blob/master/docs/reference.md>.

- Check a file or directory for spelling mistakes:

`typos {{path/to/file_or_directory}}`

- Fix typos automatically in a file or directory:

`typos {{[-w|--write-changes]}} {{path/to/file_or_directory}}`

- Preview the changes before applying them:

`typos --diff {{path/to/file_or_directory}}`

- Check a file or directory, including hidden files and directories:

`typos --hidden {{path/to/file_or_directory}}`

- Check a file or directory, ignoring files that match a specific glob pattern:

`typos --exclude {{pattern}} {{path/to/file_or_directory}}`

- Write the current configuration to a specific file:

`typos --dump-config {{path/to/typos.toml}}`

- List all supported file types:

`typos --type-list`

- Show spelling mistakes in a specific output format (defaults to `long`):

`typos --format {{brief|long|json|...}} {{path/to/file_or_directory}}`
