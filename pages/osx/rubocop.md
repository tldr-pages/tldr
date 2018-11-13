# rubocop

> Lint Ruby files.

- Check all files in the current directory (including subdirectories):

`rubocop`

- Check one or more specific files or directories:

`rubocop {{path/to/file}} {{path/to/directory}}`

- Write output to file:

`rubocop --out {{path/to/file}}`

- View list of cops (linter rules):

`rubocop --show-cops`

- Exclude a cop:

`rubocop --except {{cop_1}} {{cop_2}}`

- Run only specified cops:

`rubocop --only {{cop_1}} {{cop_2}}`

- Auto-correct files (experimental):

`rubocop --auto-correct`
