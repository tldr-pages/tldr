# rubocop

> Lint Ruby files.
> More information: <https://docs.rubocop.org/rubocop/usage/basic_usage.html>.

- Check all files in the current directory (including subdirectories):

`rubocop`

- Check one or more specific files or directories:

`rubocop {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Write output to file:

`rubocop --out {{path/to/file}}`

- View list of cops (linter rules):

`rubocop --show-cops`

- Exclude a cop:

`rubocop --except {{cop1 cop2 ...}}`

- Run only specified cops:

`rubocop --only {{cop1 cop2 ...}}`

- Auto-correct files (experimental):

`rubocop --auto-correct`
