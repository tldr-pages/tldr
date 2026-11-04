# gtrash

> A featureful trash manager, alternative to `rm` and `trash-cli`.
> More information: <https://github.com/umlx5h/gtrash#usage>.

- Move files or directories to the trash can:

`gtrash put {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- List trashed files whose original path matches a `regex`:

`gtrash find {{regex}}`

- Open an interactive TUI to select and restore trashed files:

`gtrash {{[r|restore]}}`

- Permanently delete trashed files whose original path matches a `regex`:

`gtrash find {{regex}} --rm`

- Permanently delete trashed files older than a number of days:

`gtrash prune --day {{days}}`

- Display the location, number of items, and total size of each trash can:

`gtrash summary`
