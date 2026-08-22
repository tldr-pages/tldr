# gtrash

> Move files to the system trash instead of permanently deleting them.
> More information: <https://github.com/umlx5h/gtrash>.

- Move files or directories to the system trash:

`gtrash put {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- List files currently in the trash:

`gtrash find`

- Search for trashed files matching one or more regular expressions:

`gtrash find {{pattern1 pattern2 ...}}`

- Interactively select and restore trashed files:

`gtrash restore`

- Restore files matching a search without opening the interactive interface:

`gtrash find {{pattern}} --restore`

- Permanently delete files matching a search from the trash:

`gtrash find {{pattern}} --rm`
