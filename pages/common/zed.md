# zed

> Text editor designed to be fast, efficient and convenient.
> More information: <https://zed.dev/docs/#cli>.

- Open specific paths in Zed:

`zed {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Open a path in foreground and display logs:

`zed {{path/to/project}} --foreground`

- Open a path in new window:

`zed {{path/to/project}} {{[-n|--new]}}`

- Open a file at the given line number and column:

`zed {{path/to/file}}:{{line_number}}:{{column_number}}`

- Open a diff tab in Zed for two versions of a file:

`zed --diff {{path/to/old_file}} {{path/to/new_file}}`
