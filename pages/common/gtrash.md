# gtrash

> Fast CLI trash manager written in Go.
> More information: <https://github.com/umlx5h/gtrash>.

- Move files or directories to the trash:

`gtrash put {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Open an interactive TUI to restore trashed files:

`gtrash restore`

- Find and list trashed files:

`gtrash find`

- Permanently delete specific files from the trash:

`gtrash rm {{file_name}}`

- Empty all items from the trash:

`gtrash clear`

- Display trash summary and disk usage statistics:

`gtrash summary`
