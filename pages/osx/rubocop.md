# rubocop

> Lint Ruby files.

- Check all files in the current directory:

`rubocop`

- Check specific files or directories:

`rubocop {{path_1}} {{path_2}}`

- Write output to file:

`rubocop --out {{file}}`

- View list of cops:

`rubocop --show-cops`

- Exclude a cop:

`rubocop --except {{cop_1}} {{cop_2}}`

- Run only specified cops:

`rubocop --only {{cop_1}} {{cop_2}}`

- Auto-correct files (experimental):

`rubocop --auto-correct`
