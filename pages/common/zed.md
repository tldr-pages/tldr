# zed

> Text editor designed to be fast, efficient and convenient.
> More information: <https://zed.dev/docs/#cli>.

- Open specific paths in zed:

`zed {{path/to/directory_or_file1 path/to/directory_or_file2 ...}}`

- Open a path in foreground and display logs:

`zed {{path/to/project}} --foreground`

- Open a path in new window:

`zed {{path/to/project}} {{[-n|--new]}}`

- Open a file at the given line number and column:

`zed {{path/to/file}}:{{line_number}}:{{column_number}}`

- Open a diff tab in zed for two versions of a file:

`zed --diff {{path/to/OLD_FILE}} {{path/to/NEW_FILE}}`
