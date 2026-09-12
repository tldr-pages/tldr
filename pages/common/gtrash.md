# gtrash

> A CLI and TUI trash manager conforming to the FreeDesktop.org trash specification.
> More information: <https://github.com/umlx5h/gtrash>.

- Move specific files or directories to the trash:

`gtrash put {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- List all files currently in the trash:

`gtrash find`

- Search for trashed files matching a `regex`:

`gtrash find {{regex_pattern}}`

- Open an interactive TUI to search and restore files:

`gtrash restore`

- Display a summary of trash size and item count:

`gtrash summary`

- Permanently remove files older than a specific number of days:

`gtrash prune --day {{days}}`

- Permanently delete all files from the trash:

`gtrash clear`
