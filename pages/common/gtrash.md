# gtrash

> A featureful trash CLI manager, alternative to `rm` and `trash-cli`.
> Moves files to the system trash can instead of permanently deleting them.
> More information: <https://github.com/umlx5h/gtrash>.

- Move a file or directory to the trash:

`gtrash put {{path/to/file_or_directory}}`

- List files in the trash:

`gtrash {{[f|find]}}`

- Restore files using an interactive TUI (navigate with `j`/`k`, select with `Space`, confirm with `Enter`):

`gtrash {{[r|restore]}}`

- Restore specific files by searching for them:

`gtrash find {{pattern}} --restore`

- Permanently delete files matching a pattern from the trash:

`gtrash find {{pattern}} --rm`

- Show the total number of items and size of the trash:

`gtrash summary`

- Remove trashed files older than a specific number of days:

`gtrash prune --day {{7}}`

- Limit the total size of the trash (e.g. remove large files until it is under 5 GB):

`gtrash prune --size {{5GB}}`
