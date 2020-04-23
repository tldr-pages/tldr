# rector

> An automated tool for updating and refactoring PHP 5.3+ code.
> More information: <https://github.com/rectorphp/rector>.

- Process a specific directory:

`rector process {{path/to/directory}}`

- Process a directory without applying changes (dry run):

`rector process {{path/to/directory}} --dry-run`

- Process a directory and apply coding standards:

`rector process {{path/to/directory}} --with-style`

- Display a list of available levels:

`rector levels`

- Process a directory with a specific level:

`rector process {{path/to/directory}} --level {{level_name}}`
