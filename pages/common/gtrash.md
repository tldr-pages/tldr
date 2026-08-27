# gtrash

> A trash CLI manager following the FreeDesktop.org Trash specification.
> Trashed files can be found, restored, and removed permanently.
> More information: <https://github.com/umlx5h/gtrash>.

- Move specific files to the trash can:

`gtrash put {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Select files to restore from the trash can interactively:

`gtrash restore`

- Restore files trashed by the last `gtrash put` execution:

`gtrash restore-group`

- List all trashed files:

`gtrash find`

- List trashed files matching specific names:

`gtrash find {{file1 dir1 ...}}`

- Restore trashed files matching a specific name:

`gtrash find {{file1}} --restore`

- Permanently remove trashed files matching a specific name:

`gtrash find {{file1}} --rm`

- Display a summary of all trash cans:

`gtrash summary`
